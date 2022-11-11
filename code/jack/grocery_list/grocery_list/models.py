from django.db import models

class GroceryItem(models.Model):
    item_text = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    complete_date = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField()

    def __str__(self):
        return self.item_text