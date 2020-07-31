from django.db import models


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
