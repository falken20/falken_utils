from django.contrib import admin

# Register your models here.

from .models import WeatherDataItem, CityItem, CountryItem

admin.site.register(WeatherDataItem)
admin.site.register(CityItem)
admin.site.register(CountryItem)
