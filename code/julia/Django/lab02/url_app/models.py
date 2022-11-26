from django.db import models

class Url(models.Model):
    short = models.CharField(max_length=6)
    long = models.TextField()

