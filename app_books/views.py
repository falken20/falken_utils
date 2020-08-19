from django.shortcuts import render
from django.http import HttpResponse
import logging
import os

from.models import BookItem, AuthorItem


def books_view(request):
    """ Show the screen with all the books order by year """

    logging.info(f'{os.getenv("ID_LOG", "")} Getting all the books in the DB')

    queryset = BookItem.objects.all().order_by('-book_year', '-id')
    template_name = 'books/books.html'

    return render(request, template_name, {'books': queryset})


def books_form(request):
    """ Show the form for adding books """

    logging.info(f'{os.getenv("ID_LOG", "")} Showing the books form')

    queryset = AuthorItem.objects.all().order_by('author_surname', 'author_name')
    template_name = 'books/books_form.html'

    return render(request, template_name, {'authors': queryset})
