from django.db import models

class Url(models.Model):
    short = models.CharField(max_length=6)
    long = models.TextField()

    def __str__(self):

        return self.short