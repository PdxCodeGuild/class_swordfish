from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem



def index(request):
    incomplete_items = GroceryItem.objects.filter(completed_field=False)
    complete_items = GroceryItem.objects.filter(completed_field=True)
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items 
    }
    return render(request, 'grocery_list/list.html', context)   

def add(request):
    description = request.POST["item_text"]
    GroceryItem.objects.create(item_text=description)
    # two ways to add to the list
    # 1. GroceryItem.objects.create(item_text=description)
    # 2. item = GroceryItem(item_text=description)
    # 2. item.save()
    # after generating the item, we need to send the user somewhere (ie the refreshed page, a confirm redirect etc.)
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, pk):
# get object, change boolean, save, redirect, make sure to update URL links after this
    item = get_object_or_404(GroceryItem, pk=pk)
    item.completed_field = True
    item.completed_date = timezone.now() if item.completed_field else None
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def incomplete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.completed_field = False
    item.completed_date = None
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))



    