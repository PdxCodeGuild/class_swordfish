from django.db import models
class UrlData(models.Model):
    original_url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=13)

def __str__(self):
        return f"Your shortened URL for: {self.original_url} is {self.short_url}"