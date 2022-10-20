import datetime


from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    item_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    completed_date = models.DateTimeField()
    completed_check = models.IntegerField(default = 0)

    def __str__(self):
        return self.item_text


