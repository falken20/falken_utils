from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import WordItem, WordTypeItem
from .utils import get_random_item, get_count_words


# def card_view(request):
# return render(request, 'english_dic/cards.html')


class CardView(generic.ListView):
    count_words = get_count_words(WordItem)

    template_name = 'english_dic/cards.html'
    queryset = get_random_item(WordItem)


def card_view(request):
    count_words = get_count_words(WordItem)
    print('ROD: count_words: ', count_words)

    template_name = 'english_dic/cards.html'
    queryset = get_random_item(WordItem)

    return render(request, template_name, {'worditem': queryset})


