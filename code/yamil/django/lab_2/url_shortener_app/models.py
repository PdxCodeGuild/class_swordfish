from django.db import models

class Url(models.Model):
    long_url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=6)
    
    def __str__(self):
        return self.long_url