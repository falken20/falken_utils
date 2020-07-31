import random
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
    # Looking for a valid id because the model has deletions
    while True:
        pk = random.randint(1, max_id)
        worditem = model.objects.filter(pk=pk).first()
        if worditem:
            return worditem