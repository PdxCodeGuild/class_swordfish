from unittest.util import _MAX_LENGTH
from django.db import models

class UrlHandler(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=200)

    def __str__(self):
        return self.short_url  #what should this return?