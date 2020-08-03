from django.urls import path

from . import views

urlpatterns = [
    # path('', views.CardView.as_view(), name='card_view'),
    path('', views.card_view, name='card_view'),
]
