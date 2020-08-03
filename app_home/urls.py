# by Richi Rod AKA @richionline / falken20

from django.urls import path

from . import views

urlpatterns = [
    path('', views.weather_view, name='weather_view'),
]
