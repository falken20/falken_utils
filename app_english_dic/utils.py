import random
from django.db import models
import logging
import os

from .models import WordItem


def get_count_words(model):
    """ Return the objects number in the model
    :return: Return integer with the number of objects
    """
    return WordItem.objects.all().count()


def __get_max_id(model):
    """ Return the max id in the model"""
    return model.objects.all().aggregate(max_id=models.Max("id"))['max_id']


def get_random_item(model):
    """ Return a random object of the model"""
    max_id = __get_max_id(model)

    #TODO: Change the print statement for Logging
    logging.info(f'{os.getenv("ID_LOG", "")} Max ID in the DB: {max_id}')

    # Looking for a valid id because the model has deletions
    while True and not max_id is None:
        pk = random.randint(1, max_id)
        worditem = model.objects.filter(pk=pk).first()
        if worditem:
            return worditem