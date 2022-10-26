from django.db import models
from django.contrib import admin

class Groceries(models.Model):
    item_description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    completed_item = models.BooleanField(default=False)

    # grocery_list = models.CharField(max_length=100)


    def __str__(self):
        return self.item_description

    # def index(self):
    #     return self.grocery_list
    # def add_items(request, item_id):
    #     item = Item.objects.get(pk=item_id)
    #     list_of_items =List_of_items.objects.get_or_create(us) 




# Create your models here.
