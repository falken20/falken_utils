from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
import logging
import os

from .models import WordItem, WordTypeItem
from .utils import get_random_item, get_count_words


def card_view_test(request):
    return render(request, 'english_dic/cards.html')


def card_view(request):
    """ Show one card about a english random word from the DB """

    count_words = get_count_words(WordItem)
    logging.info(f'{os.getenv("ID_LOG", "")} Number of words in the DB: {count_words}')

    template_name = 'english_dic/cards.html'
    queryset = None

    if count_words != 0:  # If the table is not empty
        queryset = get_random_item(WordItem)
        # Increase the number of times it appears, check if the field is NoneType
        if queryset.word_times:
            queryset.word_times += 1
        else:
            queryset.word_times = 1
        queryset.save()

    return render(request, template_name, {'worditem': queryset})


"""
class CardView(generic.ListView):
    count_words = get_count_words(WordItem)

    template_name = 'english_dic/cards.html'
    queryset = get_random_item(WordItem)
"""


def wordtype_form(request):
    """ Show the form for adding types of words """

    logging.info(f'{os.getenv("ID_LOG", "")} Show the form for adding types of word')

    template_name = 'english_dic/wordtypes_form.html'

    # If it comes for adding another type (add_typeword)
    message = ''
    if request.GET.get('status', None) == 'OK':
        message = 'WordType successfully saved!!'

    return render(request, template_name, {'message': message})


def add_wordtype(request):
    """ Insert a new type of word in the DB """

    logging.info(f'{os.getenv("ID_LOG", "")} Starting to add a type of word in the DB')

    wordtypeitem = WordTypeItem(word_type_id=request.POST['word_type_id'],
                                word_type=request.POST['word_type'])
    wordtypeitem.save()

    logging.info(f'{os.getenv("ID_LOG", "")} Type of word "{wordtypeitem}" successfully saved in the DB')

    return HttpResponseRedirect('/cards/new_wordtype?status=OK')


def word_form(request):
    """ Show the form for adding words """

    logging.info(f'{os.getenv("ID_LOG", "")} Show the form for adding englsh and spanish words')

    template_name = 'english_dic/words_form.html'

    queryset = WordTypeItem.objects.all().order_by('word_type')

    return render(request, template_name, {'wordtypes': queryset})


def add_word(request):
    """ Insert a new word in the DB """

    logging.info(f'{os.getenv("ID_LOG", "")} Starting to add a word in the DB')

    # Get the WordTypeItem selected
    wordtype_item = WordTypeItem.objects.get(word_type_id=request.POST['word_type_id'])

    WordItem(word_en=request.POST['word_en'],
             word_es=request.POST['word_es'],
             word_type=wordtype_item)

    logging.info(f'{os.getenv("ID_LOG", "")} Word "{request.POST["word_en"]}" successfully saved in DB')

    return HttpResponseRedirect('/cards/')
