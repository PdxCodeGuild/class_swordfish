from django.db import models
import re

class UrlShortener(models.Model):
    code = models.CharField(max_length=11)
    url = models.URLField(max_length=350)
    clicks = models.IntegerField(default=0)

    def long_url_domain(self):
        pattern = r'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)'
        domain = re.search(pattern, self.url, re.IGNORECASE)
        return domain.group(1)
    
    def __str__(self):
        return self.code + self.url