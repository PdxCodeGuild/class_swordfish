from django.db import models

class GroceryItem(models.Model):
    description = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    completed_date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description


