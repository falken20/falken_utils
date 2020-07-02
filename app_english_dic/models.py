from django.db import models
import random


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


class WordTypeItem(models.Model):
    """ Class for the different types of words: name, adjective, adverb, etc."""
    word_type = models.TextField()

    def __str__(self):
        return self.word_type


class WordItem(models.Model):
    """ Class for word in english and spanish"""
    word_en = models.TextField()
    word_es = models.TextField()
    word_type = models.ForeignKey(WordTypeItem, on_delete=models.PROTECT)
    word_times = models.IntegerField(default=0)  # Times this word was shown

    class Meta:
        """ Model metadata is “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names (verbose_name and
        verbose_name_plural). None are required, and adding class Meta to a model is completely optional."""
        verbose_name = "English/Spanish Word"
        verbose_name_plural = "English/Spanish Words"

    def __str__(self):
        return self.word_en + ' - ' + self.word_es
