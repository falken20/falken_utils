from django.contrib import admin

# ROD: Register your models here and you can use in admin console

from .models import WordTypeItem, EnglishItem

admin.site.register(WordTypeItem)
admin.site.register(EnglishItem)