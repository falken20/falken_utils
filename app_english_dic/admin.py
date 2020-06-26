from django.contrib import admin

# ROD: Register your models here and you can use in admin console

from .models import WordTypeItem, WordItem

admin.site.register(WordTypeItem)
# admin.site.register(EnglishItem)


class WordAdmin(admin.ModelAdmin):
    # Set up fields for filters
    list_filter = ['word_en', 'word_es']
    # Set up search fields
    search_fields = ['word_en', 'word_es']


admin.site.register(WordItem, WordAdmin)