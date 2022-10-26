from django.db import models

class URLApp(models.Model):
    long_url = models.URLField(max_length=200)
    short_url = models.SlugField(max_length=6)

    def __str__(self):
        return self.short_url