from django.db import models


class AuthorItem(models.Model):
    """ Class for save the different authors. """
    author_name = models.TextField()

    def __str__(self):
        return self.author_name


class BookItem(models.Model):
    """ Class for save the different books. """
    book_year = models.IntegerField(max_length=4)
    book_title = models.TextField()
    book_author = models.ForeignKey(AuthorItem, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.book_title} / {self.book_author} - {self.book_year}'

