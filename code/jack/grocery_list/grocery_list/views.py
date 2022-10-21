from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem


def index(request):
    incomplete_items = GroceryItem.objects.filter(complete=False)
    completed_items = GroceryItem.objects.filter(complete=True)
    #     if request.method=='POST':

    #     else: # if not creating new item
    #         for item in incomplete_items:
    #             if str(item.id) + ' complete' in request.POST:
    #                 item.complete = True
    #                 item.complete_date = datetime.now()
    #                 item.save()
    #             elif str(item.id) + ' delete' in request.POST:
    #                 item.delete()
    #         incomplete_items = GroceryItem.objects.filter(complete=False) # update list
    return render(request, 'grocery_list/index.html', {'incomplete_items':incomplete_items, 'completed_items':completed_items})

def add(request):
    new_item = request.POST['new_item']
    if len(new_item.replace(' ','')) > 0: # checks if input is empty or only spaces
        x = GroceryItem(item_text=new_item.capitalize(), create_date=datetime.now(), complete_date=None, complete=0)
        x.save()
    incomplete_items = GroceryItem.objects.filter(complete=False)
    completed_items = GroceryItem.objects.filter(complete=True)
    return HttpResponseRedirect("../")

def complete(request, item_id):
    item = get_object_or_404(GroceryItem.objects.get(id=item_id))
    item.complete = True
    item.complete_date = datetime.now()
    item.save()
    return HttpResponseRedirect("../")



    
