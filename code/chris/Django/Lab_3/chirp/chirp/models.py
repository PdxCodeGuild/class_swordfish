from django.db import models
from django.urls import reverse

class ChirpApp(models.Model):
    chirp = models.TextField(max_length=200)
    chirper = models.ForeignKey('auth.User', related_name='chirps', on_delete=models.CASCADE)  #related_name - used for reverse lookup vs. using default
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chirp
