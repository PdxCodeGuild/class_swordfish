from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem

# Create your views here.

def index(request):
   incompleted_items = GroceryItem.objects.filter(completed=False).ordered_by('created_date')
   completed_items = GroceryItem.objects.filter(completed=True)
   context = {'incompleted_items':incompleted_items, 
      'completed_items':completed_items}
   return render(request, 'grocery_list/index.html', context)


def add(request):
   text_description = request.POST["description"]
   item = GroceryItem(description=text_description)
   item.save()
   return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, pk):
   item = get_object_or_404(GroceryItem, pk=pk)
   if item.completed:
      item.completed = False
      item.completed_date = None
   else:
      item.completed = True 
      item.completed_date = timezone.now()
      item.save()  
      return HttpResponseRedirect(reverse('grocery_list:index'))


def delete(request, pk):
   item = get_object_or_404(GroceryItem, pk=pk)
   item.delete()
   return HttpResponseRedirect(reverse('grocery_list:index'))
   
