from django.db import models

class GroceryItems(models.Model):
    item_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    item_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name


    
