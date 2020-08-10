# by Richi Rod AKA @richionline / falken20

"""
Functions for load data files and initialize DBs
"""

import pandas as pd
import logging
import os
from sqlalchemy import create_engine
import dj_database_url  # For returning a Django database connection dictionary
import csv


BOOKS_CSV_NAME = '../init_files_load/books.csv'
BOOKS_DB_TABLE = 'app_books_bookitem'

AUTHORS_CSV_NAME = '../init_files_load/authors.csv'
AUTHORS_DB_TABLE =  'app_books_authoritem'

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


def load_csv_books():
    """ Process to load data books for the initial charge """
    logging.info(f'{os.getenv("ID_LOG", "")} Starting to load Books from CSV file...')

    csv_file = csv.reader(open(BOOKS_CSV_NAME,mode='r'))
    next(csv_file) # Jump to the next row after the header
    for row in csv_file:
        pass

    logging.info(f'{os.getenv("ID_LOG", "")} Load books successfully!!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Create the engine instance "<dbms>://<username>:<password>@<hostname>:<port>/<db_name>"
    db = DATABASES['default']
    url_db = f'postgres://{db["USER"]}:{db["PASSWORD"]}@{db["HOST"]}:{db["PORT"]}/{db["NAME"]}'
    logging.info(f'{os.getenv("ID_LOG", "")} url db: {url_db}')
    engine = create_engine(url_db)

    engine.

    load_csv_authors()
