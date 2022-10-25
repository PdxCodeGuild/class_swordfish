from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    creation_ip = models.CharField(max_length=200)
    clicks = models.CharField(max_length=8)

    def __str__(self):
        return self.code