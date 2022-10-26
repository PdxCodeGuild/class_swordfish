from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . models import Groceries

def index(request):
    not_complete = Groceries.objects.filter(completed_item=False)
    completed_items = Groceries.objects.filter(completed_item=True)
    context ={'incomplete_items': not_complete,
    'completed_items': completed_items
    }
    return render(request, 'Grocery_List/index.html', context)

def add(request):
    description = request.POST["text_description"]
    Groceries.objects.create(text_description=description)
    return HttpResponseRedirect(reverse('Grocery_List:index'))

def completed(request, pk):
    item = get_object_or_404(Groceries, pk=pk)
    if item.completed_item:
        item.completed_item=False
    else: 
        item.completed_item=True
        item.save()
    return HttpResponseRedirect(reverse('Grocery_List:index'))

def delete(request, pk):
    item = get_object_or_404(Groceries, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('Grocery_List:index'))

    






# def grocery_list(request):
#     grocery_items = get_object_or_404()
# Create your views here.
