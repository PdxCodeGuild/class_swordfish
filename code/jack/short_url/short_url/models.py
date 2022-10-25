from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.code