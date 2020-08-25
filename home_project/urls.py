"""home_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views as project_views
from app_home import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # About page
    path('about/', project_views.about_view, name='about'),

    # Home page
    path('', views.weather_view, name='home'),

    # About To_Do app
    path('todo/', include('app_todo.urls')),

    # About English Dic app
    path('cards/', include('app_english_dic.urls')),

    # About Home app
    path('house/', include('app_home.urls')),

    # About Books app
    path('books/', include('app_books.urls')),
]
