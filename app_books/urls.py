from django.urls import path

from . import views

urlpatterns = [
    path('', views.books_view, name='books_view'),
    path('add_book/', views.books_form, name='add_book'),
]