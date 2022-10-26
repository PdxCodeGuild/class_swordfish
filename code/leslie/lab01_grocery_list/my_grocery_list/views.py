from django.shortcuts import render, get_object_or_404
from .models import GroceryItem
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def index(request):
    # items = GroceryItem.objects.all()
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('date_created') #order -- newest things get added to bottom
    completed_items = GroceryItem.objects.filter(completed=True).order_by('-date_completed')
    context = {
        "incomplete_items": incomplete_items,
        "completed_items": completed_items
    }
    return render(request, 'my_grocery_list/index.html', context) #RENDER puts stuff in DB, context is what it's called in index

def add(request):
    data = request.POST['item_description'] #GETS THE DATA FROM THE FORM    
    item = GroceryItem.objects.create(item_description=data)
    item.save()
    return HttpResponseRedirect(reverse('my_grocery_list:index')) #reverse means django figures out URL for me

def complete(request, pk):
    item = get_object_or_404(GroceryItem,pk=pk)
    if item.completed:
        item.completed = False
        item.date_completed = None
    else:
        item.completed = True  
        item.date_completed = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('my_grocery_list:index'))


def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('my_grocery_list:index'))

