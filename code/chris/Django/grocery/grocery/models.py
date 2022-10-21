from email.policy import default
from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    #name of field = type of field(options... with CharField - max_length is required)
    created_date = models.DateTimeField(auto_now_add=True) #how do i filter this from completed date?
    completed_date = models.DateTimeField(null=True, blank=True)
    task_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description
    #this gives string representation of the model vs. object type
