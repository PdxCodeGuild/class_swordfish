from django.db import models

class Shortener(models.Model):
    url = models.CharField(max_length = 200)
    code = models.CharField(max_length = 15)

    def __str__(self):
	    return self.url