# by Richi Rod AKA @richionline / falken20

"""
Functions for load data files and initialize DBs
"""

import pandas as pd
import logging
import os
import sys
from sqlalchemy import create_engine
import dj_database_url  # For returning a Django database connection dictionary
import csv
import psycopg2


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOKS_CSV_NAME = os.path.join(BASE_DIR, 'init_files_load/bookitem.csv')
BOOKS_DB_TABLE = 'app_books_bookitem'
AUTHORS_CSV_NAME = os.path.join(BASE_DIR, 'init_files_load/authoritem.csv')
AUTHORS_DB_TABLE = 'app_books_authoritem'

WORDTYPES_CSV_NAME = os.path.join(BASE_DIR, 'init_files_load/wordtypeitem.csv')
WORDTYPES_DB_TABLE = 'app_english_dic_wordtypeitem'
WORDS_CSV_NAME = os.path.join(BASE_DIR, 'init_files_load/worditem.csv')
WORDS_DB_TABLE = 'app_english_dic_worditem'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'falken_homedb',
        'USER': 'falken_home',
        'PASSWORD': '(Falken_home-33)',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

ENV_PRO = ('ENV_PRO' in os.environ and os.environ['ENV_PRO'].upper() == 'Y')
if ENV_PRO:
    DATABASES['default'] = dj_database_url.config(default=os.getenv('DATABASE_URL'))


def load_csv_wordtypes():
    """ Process to load data words type for the initial charge """
    logging.info(f'{os.getenv("ID_LOG", "")} Starting to load Words Types from CSV file...')

    for df in pd.read_csv(WORDTYPES_CSV_NAME, chunksize=1000):
        df.to_sql(
            WORDTYPES_DB_TABLE,
            engine,
            index=False,
            if_exists='append',  # If the table already exists, append this data
        )
    logging.info(f'{os.getenv("ID_LOG", "")} Load Words Types successfully!!')


def load_csv_words():
    """ Process to load data words for the initial charge"""
    logging.info(f'{os.getenv("ID_LOG", "")} Starting to load Words from CSV file...')

    for df in pd.read_csv(WORDS_CSV_NAME, chunksize=100):
        df.to_sql(
            WORDS_DB_TABLE,
            engine,
            index=False,
            if_exists='append',  # If the table already exists, append this data
        )
        logging.info(f'{os.getenv("ID_LOG", "")} Data block of 100 rows load successfully')
    logging.info(f'{os.getenv("ID_LOG", "")} Load Words successfully!!')


def load_csv_authors():
    """ Process to load data authors for the initial charge """
    logging.info(f'{os.getenv("ID_LOG", "")} Starting to load Authors from CSV file...')

    # Reading the file in 1000 rows blocks
    for df in pd.read_csv(AUTHORS_CSV_NAME, chunksize=1000):
        df.to_sql(
            AUTHORS_DB_TABLE,
            engine,
            index=False,
            if_exists='append'  # if the table already exists, append this data
        )
    logging.info(f'{os.getenv("ID_LOG", "")} Load Authors successfully!!')


def get_connection_db():
    """ Method for get the connection to the DB """
    logging.info(f'{os.getenv("ID_LOG", "")} Getting the DB connection...')
    return psycopg2.connect(user=db["USER"],
                            password=db["PASSWORD"],
                            host=db["HOST"],
                            port=db["PORT"],
                            database=db["NAME"])


def search_author(complete_name, cursor):
    """
    Getting the id of a specific author
    :param cursor: Cursor for executing SQL statement
    :param name: Name and surname author to search
    :return: The Id of the author
    """
    try:
        # Get the name and surname from name
        author_name = complete_name.split(' ', 1)[0].strip()
        if len(complete_name.split(' ', 1)) == 2:
            author_surname = complete_name.split(' ', 1)[1].strip()
        else:
            author_surname = ''

        sql_statement = f"SELECT id FROM {AUTHORS_DB_TABLE}" \
                        f" WHERE author_name = '{author_name}'" \
                        f" AND author_surname = '{author_surname}'"

        cursor.execute(sql_statement, (author_name, author_surname,))
        row = cursor.fetchone()
        if row is not None:
            return row[0]  # Because fetchone() return a list
        else:
            return None

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f'{os.getenv("ID_LOG", "")} ERROR searching author <{complete_name}> in line'
                      f' {sys.exc_info()[2].tb_lineno}: {error}')
        return None


def save_book(book_year, book_title, book_author_id, cursor):
    """
    Save the register of the book in the DB
    :param book_year: Year when read the book
    :param book_title: Title of the book
    :param book_author_id: Author of the book
    :param cursor: Cursor for executing SQL statement
    """
    try:
        sql_statement = f'INSERT INTO {BOOKS_DB_TABLE}(book_year, book_title, book_author_id)' \
                        f' VALUES (%s, %s, {book_author_id})'

        cursor.execute(sql_statement, (book_year, book_title,))
        logging.info(f'{os.getenv("ID_LOG", "")} The book "{book_title}" successfully saved')

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f'{os.getenv("ID_LOG", "")} ERROR saving the book: "{book_title}": {error}')
        return None


def load_csv_books():
    """ Process to load data books for the initial charge """
    logging.info(f'{os.getenv("ID_LOG", "")} Starting to load Books from CSV file...')

    try:
        # Getting the connection DB and cursor for sql statements
        connection = get_connection_db()
        cursor = connection.cursor()
        num_warnings = 0
        num_books = 0

        csv_file = csv.DictReader(open(BOOKS_CSV_NAME, mode='r'))

        for row in csv_file:
            book_year = row['book_year'].strip()
            book_title = row['book_title'].strip()
            complete_name = row['author_name'].strip()

            author_id = search_author(complete_name, cursor)
            if author_id is not None:
                save_book(book_year, book_title, author_id, cursor)
                connection.commit()
                num_books += 1
            else:
                logging.warning(f'{os.getenv("ID_LOG", "")} Impossible to find the author for the book "{book_title}"')
                num_warnings += 1

        logging.info(f'{os.getenv("ID_LOG", "")} Load books finished!!. Books: {num_books}, Warnings: {num_warnings}')

    except (Exception, psycopg2.DatabaseError) as error:
        # TODO: Insert error line in rest of the logging.error as this below line
        logging.error(f'{os.getenv("ID_LOG", "")} ERROR loading books in line {sys.exc_info()[2].tb_lineno}: {error}')

    finally:
        if connection:
            cursor.close()
            connection.close()
        logging.info(f'{os.getenv("ID_LOG", "")} DB connection is closed')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    print('************ INITIAL CHARGES UTILITY ************')

    # Create the engine instance "<dbms>://<username>:<password>@<hostname>:<port>/<db_name>"
    db = DATABASES['default']
    url_db = f'postgres://{db["USER"]}:{db["PASSWORD"]}@{db["HOST"]}:{db["PORT"]}/{db["NAME"]}'
    logging.info(f'{os.getenv("ID_LOG", "")} url db: {url_db}')
    engine = create_engine(url_db)

    # About english words
    print('\n****** ENGLISH / SPANISH WORDS ******')
    load_csv_wordtypes() if input('Load word types? (Y/n)') == 'Y' else print('Skipping load word types')
    load_csv_words() if input('Load english words? (Y/n)') == 'Y' else print('Skipping load english words')

    # About Books
    print('\n****** BOOKS ******')
    load_csv_authors() if input('Load book authors? (Y/n)') == 'Y' else print('Skipping load book authors')
    load_csv_books() if input('Load books? (Y/n)') == 'Y' else print('Skipping load books')
