from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    item = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True) 
    completed_date = models.DateTimeField(null=True, blank=True)
    item_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item