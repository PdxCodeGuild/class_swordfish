from django.db import models

import datetime
from django.utils import timezone

# Create your models here.

# Model convention states that the model name should be capitalized
class GroceryItem(models.Model):
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    # blank = True for Django, and null = True will allow the database to be empty.
    # blank = true allows it to be blank upon generation in the database, null=true allows it to be a nullable field, these generally come together
    completed_date = models.DateField(null=True, blank=True)
    completed_field = models.BooleanField(default=False)


    def __str__(self):
        return self.item_text