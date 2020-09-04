# by Richi Rod AKA @richionline / falken20

import os
import logging
from django.shortcuts import render
from django.utils.timezone import now
from django.http import HttpResponse, HttpResponseRedirect

from .utils import scrap_web
from .models import CountryItem, CityItem, WeatherDataItem

URL_WEATHER = 'http://meteomad.net/estaciones/cercedilla/cercedilla.htm'


def weather_view(request):
    """ For getting temperature data from scrapping climate web and showing."""

    logging.info(f'{os.getenv("ID_LOG", "")} Showing the weather screen')

    # Getting a dataframe with the all data weather
    df_weather = scrap_web(URL_WEATHER)

    dict_weather = df_weather.to_dict(orient='records')

    # TODO: In some momment the city should be choosed by the user
    city = 'Cercedilla'

    return render(request, 'house/weather.html', {'data_weather': dict_weather, 'city': city, 'time': now()})


def country_form(request):
    """ Show the form for adding countries """

    logging.info(f'{os.getenv("ID_LOG", "")} Showing the country form')

    queryset_country = CountryItem.objects.all().order_by('country_name')
    template_name = 'house/country_form.html'

    # If it comes for adding another item
    message = ''
    if request.GET.get('status', None) == 'OK':
        message = 'Country successfully saved!!'

    return render(request, template_name, {'countries': queryset_country, 'message': message})


def add_country(request):
    """ Insert a new country in DB """

    logging.info(f'{os.getenv("ID_LOG", "")} Starting to add a country in the DB')

    country_item = CountryItem(country_name=request.POST['country_name']).save()

    logging.info(f'{os.getenv("ID_LOG", "")} Country "{country_item}" successfully saved in the DB')

    return HttpResponseRedirect('/house/new_country?status=OK')


def city_form(request):
    """ Show the form for adding cities """

    logging.info(f'{os.getenv("ID_LOG", "")} Showing the cities form')

    template_name = 'house/city_form.html'
    queryset_country = CountryItem.objects.all().order_by('country_name')
    queryset_city = CityItem.objects.all().order_by('city_name')

    # If it comes for adding another item
    message = ''
    if request.GET.get('status', None) == 'OK':
        message = 'Country successfully saved!!'

    return render(request, template_name, {'countries': queryset_country,
                                           'cities': queryset_city,
                                           'message': message})


def add_city(request):
    """ Insert a new city in DB """

    logging.info(f'{os.getenv("ID_LOG", "")} Starting to add a city in the DB')

    # Get the country item
    country_item = CountryItem.objects.get(id=request.POST['country_id'])

    city_item = CityItem(city_name=request.POST['city_name'],
                         country_name=country_item,
                         weather_url=request.POST['weather_url']).save()

    logging.info(f'{os.getenv("ID_LOG", "")} City "{city_item}" successfully saved in the DB')

    return HttpResponseRedirect('/house/new_city?status=OK')


def weather_report_view(request):
    """ Show last weather data in the DB """

    logging.info(f'{os.getenv("ID_LOG", "")} Starting to show weather data day')

    template_name = 'house/weather_report.html'
    today = now()
    queryset = WeatherDataItem.objects.filter(weather_date__year=today.year,
                                              weather_date__month=today.month,
                                              weather_date__day=today.day).order_by('-weather_date')

    return render(request, template_name, {'weather_data': queryset})
