from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from.models import GroceryItem

def index(request):
    grocery_list = GroceryItem.objects.order_by('-created_date')
    return render(request, 'grocery/index.html', {'grocery_list':grocery_list})

def form(request, grocery_item):
    return HttpResponse(f'Please enter in a grocery item {grocery_item}')

def complete(request, grocery_item):
    return HttpResponse(f'Check-off what is completed {grocery_item}')

def delete(request, grocery_item):
    return HttpResponse(f'Which item would you like to delete {grocery_item}')