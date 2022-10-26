
from django.db import models

class Switch(models.Model):
    long_url = models.URLField()
    code = models.CharField(max_length = 10)

    def __str__(self):
        return self.long_url
