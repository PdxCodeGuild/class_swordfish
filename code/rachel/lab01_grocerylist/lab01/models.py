from django.db import models
# * 1 x grocery item model

class GroceryItem(models.Model):
    description = models.CharField(max_length=50)
    created_date = models.DateTimeField
    completed_date = models.DateTimeField
    # completed_question = 