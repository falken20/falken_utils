from django.shortcuts import render
from django.http import HttpResponse
import logging
import os

from.models import BookItem, AuthorItem


def books_view(request):

    logging.info(f'{os.getenv("ID_LOG", "")} Getting all the books in the DB')

    queryset = BookItem.objects.all().order_by('-book_year', '-id')
    template_name = 'books/books.html'

    return render(request, template_name, {'books': queryset})
