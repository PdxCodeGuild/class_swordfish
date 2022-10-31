from django.db import models

# Create your models here.
class OriginalURL(models.Model):
    url_link = models.CharField(max_length=1000)
    url_link_id = models.CharField(max_length = 7)

    def __str__(self):
        return self.url_link_id