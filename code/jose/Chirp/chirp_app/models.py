from django.db import models
from django.urls import reverse 

class Chirp(models.Model):
    chirp = models.CharField(max_length=200)
    chirper = models.CharField(max_length= 100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chirp
    
    def get_absolute_url(self):
        return reverse('chirp')


    
    

# Create your models here.
