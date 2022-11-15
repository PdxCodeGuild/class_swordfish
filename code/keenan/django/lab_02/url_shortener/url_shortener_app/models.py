from django.db import models

# Create your models here.
class Url(models.Model):
    long_text = models.CharField(max_length=200)
    shortened_code = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.long_text