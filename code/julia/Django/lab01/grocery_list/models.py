from django.db import models

class GroceryItem(models.Model):
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.description


