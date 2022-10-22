import datetime
from sqlite3 import complete_statement
from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
	item_text = models.CharField(max_length = 100)
	created_date = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
	complete = models.BooleanField(default = False)

	def __str__(self):
		return self.item_text