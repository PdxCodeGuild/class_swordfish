from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    image = models.URLField()

    def __str__(self):
        return self.name

class Type(models.Model):
    type = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemon, related_name='types')


    def __str__(self):
        return self.type
