
import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Chirp(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("chirp:detail", args={self.pk})
