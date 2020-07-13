from django.shortcuts import render
from django.http import HttpResponse


def books_view(request):
    return HttpResponse('<h1> Booooooks!!!! </h1>')