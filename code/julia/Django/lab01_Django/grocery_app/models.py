from django.db import models
from django.contrib.auth.models import User

class GroceryList(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
   description = models.CharField(max_length=200)
   date_created = models.DateTimeField(auto_now_add=True)
   date_completed = models.DateTimeField(blank=True, null=True)


   def __str__(self):
    return self.description

class Meta:
    ordering = ['date_completed']