from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem


def index(request):
    complete_items = GroceryItem.objects.filter(completed=True)
    incomplete_items = GroceryItem.objects.filter(completed=False)
    context= {
        'complete_items' : complete_items,
        'incomplete_items' : incomplete_items,
        }
    return render(request, 'index.html', context)

def add(request):
    add_item = request.POST['list_text']
    item = GroceryItem(list_text=add_item)
    item.save()
    return HttpResponseRedirect(reverse('grocery_app:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_app:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.completed == True:
        item.completed = False
        item.completed_time = None
    else:
        item.completed = True
        item.completed_time = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_app:index'))

    
    
