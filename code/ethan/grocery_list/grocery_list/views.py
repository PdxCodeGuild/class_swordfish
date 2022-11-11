from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import GroceryItem
from django.db import models


def index(request):
    incomplete_items = GroceryItem.objects.filter(complete=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(complete=True).order_by('-complete_date')
    context = {'incomplete_items': incomplete_items, 'completed_items': completed_items}
    return render(request, 'index.html', context)

def add(request):
    description = request.POST["item_text"]
    item = GroceryItem(item_text=description)
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    if item.complete:
        item.complete = False
        item.complete_date = None
    else:
        item.complete = True
        item.complete_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))