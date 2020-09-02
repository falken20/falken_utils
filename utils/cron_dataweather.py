"""
Cron for processing every day the data of weather and save in the DB
"""

import logging
import os
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from django.utils.timezone import now

from app_home.utils import scrap_web
from app_home.models import CityItem, WeatherDataItem

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home_project.settings')
django.setup()


URL_WEATHER = 'http://meteomad.net/estaciones/cercedilla/cercedilla.htm'
# This constant is for to know the position in the dict of the values
POSITION_TEMP = 0
POSITION_RAIN = 5
POSITION_HUMI = 1
POSITION_WIND = 3


def load_weather_data():
    """ Process to load weather data in the DB """
    logging.info(f'{os.getenv("ID_LOG", "")} Starting to load weather data...')

    try:
        # Getting a dataframe with the all data weather
        df_weather = scrap_web(URL_WEATHER)

        # Transform to a list of dict, each dict with "Parameter" and "Value"
        dict_weather = df_weather.to_dict(orient='records')

        city_item = CityItem.objects.filter(city_name='Cercedilla')
        if city_item:
            WeatherDataItem(weather_temp = dict_weather[POSITION_TEMP]['Value'],
                            weather_rain = dict_weather[POSITION_RAIN]['Value'],
                            weather_humidity = dict_weather[POSITION_HUMI]['Value'],
                            weather_wind = dict_weather[POSITION_WIND]['Value'],
                            weather_date=now(),
                            city_name=city_item).save()
            logging.info(f'{os.getenv("ID_LOG", "")} Save weather data ok at: {now()}')
        else:
            logging.error(f'{os.getenv("ID_LOG", "")} Problems to find the city to save weather data')

    except (Exception) as error:
        logging.error(f'{os.getenv("ID_LOG", "")} ERROR saving weather data {sys.exc_info()[2].tb_lineno}: {error}')


cron_data_weather = BlockingScheduler()


# The cron executes every day and every hour at 59 minutes (by default day, hour and others params is *)
# It is no neccesary set hour=* because is a default value
@cron_data_weather.scheduled_job('cron', day_of_week='mon-sun', hour='*', minute=59)
def scheduled_cron_data_weather():
    """ Process to get the temperature and rain data every hour and to save in DB """

    logging.info(f'{os.getenv("ID_LOG", "")} ************ START CRON DATA WEATHER ************')

    load_weather_data()


cron_data_weather.start()






