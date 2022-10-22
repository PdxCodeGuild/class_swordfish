from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    item_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.item_text