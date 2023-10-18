from django.urls import path

from . import views

urlpatterns = [
    path('', views.books_view, name='books_view'),
    path('new_book/', views.books_form, name='form_new_book'),
    path('add_book/', views.add_book, name='create_new_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    path('new_author/', views.authors_form, name='form_new_author'),
    path('add_author/', views.add_author, name='create_new_author'),
    path('delete_author/<int:author_id>/', views.delete_author, name='delete_author'),

    path('books_report', views.books_report_view, name='report_books'),
]