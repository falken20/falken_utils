# by Richi Rod AKA @richionline / falken20

from django.urls import path
from app_users import views

urlpatterns = [
    path('welcome', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]