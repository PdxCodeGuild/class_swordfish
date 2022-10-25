from django.db import models

class CodeStorage(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url