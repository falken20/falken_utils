from django.urls import path

from . import views

urlpatterns = [
    path('new_book/', views.books_form, name='new_book'),
    path('add_book/', views.add_book, name='add_book'),
]