# by Richi Rod AKA @richionline / falken20

from django.shortcuts import render
from django.utils.timezone import now

from .utils import scrap_web

URL_WEATHER = 'http://meteomad.net/estaciones/cercedilla/cercedilla.htm'


def weather_view(request):
    """ For getting temperature data from scrapping climate web and showing."""

    # Getting a dataframe with the all data weather
    df_weather = scrap_web(URL_WEATHER)

    dict_weather = df_weather.to_dict(orient='records')
    # TODO: In some momment the city should be choosed by the user
    city = 'Cercedilla'

    return render(request, 'home/weather.html', {'data_weather': dict_weather, 'city': city, 'time': now()})
