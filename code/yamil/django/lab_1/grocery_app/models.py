from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    list_text = models.CharField(max_length=200, default="")
    completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=timezone.now)
    completed_time = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.list_text