from django.db import models

import datetime
from django.utils import timezone

# Create your models here.

# Model convention states that the model name should be capitalized
class GroceryItem(models.Model):
    item_text = models.CharField(max_length=200)
    # note: could i have an error message if the max max_len is exceeded?
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateField(null=True, blank=True)
    completed_field = models.BooleanField(default=False)


    # note: from advanced ORM from the models notes? below caused an error'Field__init__() got an unexpected argument' from the isnull value so using above
    # purchased = models.BooleanField(completed_date__isnull=False)
    # example in notes is:completed_items = TodoItem.objects.filter(date_completed__isnull=False)


    def __str__(self):
        return self.item_text