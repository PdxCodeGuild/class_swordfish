from django.db import models

class UrlApp(models.Model):
    url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=6)

    def __str__(self):
        return self.url