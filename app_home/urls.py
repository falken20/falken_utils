# by Richi Rod AKA @richionline / falken20

from django.urls import path

from . import views

urlpatterns = [
    path('', views.weather_view, name='weather_view'),

    path('new_country/', views.country_form, name='form_new_country'),
    path('add_country/', views.add_country, name='create_new_country'),

    path('new_city/', views.city_form, name='form_new_city'),
    path('add_city/', views.add_city, name='create_new_city'),

    path('weather_report', views.weather_report_view, name='report_weather'),
]
