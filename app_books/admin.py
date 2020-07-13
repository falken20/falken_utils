from django.contrib import admin

from .models import AuthorItem, BookItem

admin.site.register(AuthorItem)


class BookAdmin(admin.ModelAdmin):
    list_filter = ['book_author', 'book_year']
    search_fields = ['book_title', 'book_author', 'book_year']


admin.site.register(BookItem, BookAdmin)