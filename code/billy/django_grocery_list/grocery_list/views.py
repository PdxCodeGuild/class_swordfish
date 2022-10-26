from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItems

def index(request):
    incomplete_items = GroceryItems.objects.filter(item_completed=False).order_by('created_date')
    completed_items = GroceryItems.objects.filter(item_completed=True).order_by('-completed_date')
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items
    }
    return render(request, 'grocery_list/index.html', context)

def add(request):
    item_description = request.POST['item_name']
    GroceryItems.objects.create(item_name=item_description)
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItems, pk=pk)
    item.item_completed = True
    item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItems, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))
