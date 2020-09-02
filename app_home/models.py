from django.db import models
from django.utils.timezone import now


class CountryItem(models.Model):
    """ Class to stock the countries """
    country_name = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.country_name}'


class CityItem(models.Model):
    """ Class to stock cities """
    city_name = models.TextField(max_length=50)
    country_name = models.ForeignKey(CountryItem, on_delete=models.PROTECT)
    weather_url = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.city_name} ({self.country_name})'


class WeatherDataItem(models.Model):
    """ Class to stock the weather data """
    weather_temp = models.FloatField()
    weather_rain = models.FloatField()
    weather_humidity = models.FloatField()
    weather_wind = models.FloatField()
    weather_date = models.DateTimeField(default=now)
    city_name = models.ForeignKey(CityItem, on_delete=models.PROTECT)

    def __str__(self):
        return f'The weather data in {self.city_name} at {self.weather_date} ' \
               f'is ☀️ {self.weather_temp}️º / 🌧 {self.weather_rain}mm' \
               f', {self.weather_humidity}% humidity' \
               f' and {self.weather_wind}Km/h wind'
