from django.contrib import admin

# ROD: Register your models here and you can use in admin console

from .models import TodoItem

admin.site.register(TodoItem)