from email.policy import default
from django.db import models

class GroceryItem(models.Model):
    item_description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True) #says field can be blank
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.item_description
