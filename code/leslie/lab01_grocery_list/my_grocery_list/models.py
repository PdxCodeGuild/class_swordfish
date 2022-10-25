from email.policy import default
from django.db import models

class GroceryItem(models.Model):
    item_description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_completed = models.DateField(auto_now_add=True)
    item_completed = models.BooleanField(default=False)
    item_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.item_description