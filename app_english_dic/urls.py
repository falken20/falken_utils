from django.urls import path

from . import views

urlpatterns = [
    # path('', views.CardView.as_view(), name='card_view'),
    path('', views.card_view, name='card_view'),

    path('new_wordtype/', views.wordtype_form, name='form_new_wordtype'),
    path('add_wordtype/', views.add_wordtype, name='create_new_wordtype'),

    path('new_word/', views.word_form, name='form_new_word'),
    path('add_word/', views.add_word, name='create_new_word'),

    path('words_top_report', views.words_report_view, name='report_words_top'),
]
