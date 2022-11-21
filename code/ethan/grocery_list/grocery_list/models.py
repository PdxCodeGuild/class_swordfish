import datetime
from sqlite3 import complete_statement
from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
	item_text = models.CharField(max_length = 100)
	created_date = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default = False)
	complete_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.item_text

