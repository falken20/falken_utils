from django.db import models
from django.utils.timezone import now


class TodoItem(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(default=now)
