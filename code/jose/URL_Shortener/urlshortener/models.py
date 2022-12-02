from django.db import models
import random 
# Create your models here.
class URL_Shortener(models.Model):
    original_url = models.CharField(max_length=250)
    new_url = models.CharField(max_length=150)
    

    def __str__(self):
        return self.original_url