from django.db import models

class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text_description