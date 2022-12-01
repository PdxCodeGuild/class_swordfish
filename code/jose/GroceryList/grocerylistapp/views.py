from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from .models import GroceryItem


def index(request):
    incomplete_items = GroceryItem.objects.filter(item_completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(item_completed=True).order_by('-completed_date')
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items
    }
    return render(request, 'grocery_list/index.html', context)

def add(request):
    item_description = request.POST['item']
    GroceryItem.objects.create(item=item_description)
    return HttpResponseRedirect(reverse('grocerylistapp:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.item_completed = True
    item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocerylistapp:index'))

def incomplete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.item_completed = False
    item.save()
    return HttpResponseRedirect(reverse('grocerylistapp:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocerylistapp:index'))