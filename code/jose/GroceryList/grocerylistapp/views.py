from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .models import GroceryItem


def index(request):
    incomplete_items = GroceryItem.objects.filter(complete=False)
    completed_items = GroceryItem.objects.filter(complete=True)
    return render(request, 'grocery_list/index.html', {'incomplete_items':incomplete_items, 'completed_items':completed_items})

def add(request):
    new_item = request.POST['new_item']
    if len(new_item.replace(' ','')) > 0: # checks if input is empty or only spaces
        grocery = GroceryItem(item_text=new_item.capitalize(), create_date=datetime.now(), complete_date=None, complete=0)
        grocery.save()
    incomplete_items = GroceryItem.objects.filter(complete=False)
    completed_items = GroceryItem.objects.filter(complete=True)
    return HttpResponseRedirect("../")

def complete(request, item_id):
    item = get_object_or_404(GroceryItem.objects.filter(id=item_id))
    item.item_completed = True
    item.completed_date = datetime.now()
    item.save()
    return HttpResponseRedirect("../")

def incomplete(request, item_id):
    item = get_object_or_404(GroceryItem.objects.filter(id=item_id))
    item.item_completed = False
    item.completed_date = None
    item.save()
    return HttpResponseRedirect("../")

def delete(request, item_id):
    item = get_object_or_404(GroceryItem.objects.filter(id=item_id))
    item.delete()
    return HttpResponseRedirect("../")