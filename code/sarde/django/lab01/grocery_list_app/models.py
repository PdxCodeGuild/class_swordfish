import datetime

from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    grocery_item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.Field.null
    is_completed = models.BooleanField(default=False)
        
    def __str__(self):
        return self.grocery_item_text
    
