from unittest.util import _MAX_LENGTH
from django.db import models
from .utils import create_shortened_url

class UrlHandler(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0) 
    long_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, blank=True) #blank so user can use generated url

    class Meta: #how the class must behave
        ordering = ["-created"] #ordered by the most recent ones

    def __str__(self):
        return self.short_url  #what should this return?

    def save(self, *args, **kwargs): #everytime a url object is saved, 
        if not self.short_url:       #and when the short_url isn't specified,
            self.short_url = create_shortened_url(self) #fill it with a random code
        super().save(*args, **kwargs) #and save it