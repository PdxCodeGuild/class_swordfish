from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem


def hello_world(request):
    greeting = 'hi'
    return HttpResponse(greeting)

def index(request):
    grocery_item_list = GroceryItem.objects.all()
    print('grocery item list',grocery_item_list)
    return HttpResponse('abcd')
    # return render(request, '', {})

