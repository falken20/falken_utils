from django.db import models


class AuthorItem(models.Model):
    """ Class for save the different authors. """
    author_name = models.TextField(max_length=30)
    author_surname = models.TextField(max_length=60, default='', blank=True, null=True)

    def __str__(self):
        return f'{self.author_name} {self.author_surname}'


class BookItem(models.Model):
    """ Class for save the different books. """
    book_year = models.IntegerField()
    book_title = models.TextField()
    book_author = models.ForeignKey(AuthorItem, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.book_title} / {self.book_author} - {self.book_year}'

