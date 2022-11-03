# from binascii import Incomplete
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem

def index(request):
    incomplete_items = GroceryItem.objects.filter(item_completed=False).order_by('date_created')
    completed_items = GroceryItem.objects.filter(item_completed=True).order_by('date_completed')
    context = {
        'incomplete': incomplete_items,
        'completed': completed_items
    }
    return render(request, 'grocery_app/index.html', context)


def add(request):
    item_description = request.POST['item_name']
    GroceryItem.objects.create(item_name=item_description)
    return HttpResponseRedirect(reverse('grocery_app:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.item_completed = True
    item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_app:index'))

def incomplete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.item_completed = False
    item.save()
    return HttpResponseRedirect(reverse('grocery_app:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_app:index'))


   


# def add(request):
#     return render()



# def complete(request, pk):

# def delete(request, pk):


    
    #return render(request, 'grocery_app/basis.html', context)
   # Incompleted_items = GroceryItem.objects.filter(completed=False).order_by('date_created')


# Create your views here.
