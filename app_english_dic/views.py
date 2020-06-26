from django.shortcuts import render
from django.http import HttpResponse


def card_view(request):
    return render(request, 'english_dic/cards.html')