from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

def index(request):
    items_list = GroceryItem.objects.all()
    return render(request, 'grocery_list/index.html', {'items_list':items_list})

