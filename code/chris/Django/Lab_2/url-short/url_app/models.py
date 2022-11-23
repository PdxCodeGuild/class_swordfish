from django.db import models

class CodeStorage(models.Model):
    long_url = models.URLField(max_length=200, blank=False)
    short_url = models.CharField(max_length=50, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url