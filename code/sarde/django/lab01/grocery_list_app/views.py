from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

import grocery_list_app
from .models import GroceryItem
from django.urls import reverse


def hello_world(request):
    greeting = 'hi'
    return HttpResponse(greeting)

def grocery_list(request):
    grocery_item_list = GroceryItem.objects.all()
    # print('grocery item list',grocery_item_list)
    # return HttpResponse('abcd')
    return render(request, 'grocery_list_app/grocery_list.html', {'grocery_item_list': grocery_item_list})

def add(request):
    #data <QueryDict: {'csrfmiddlewaretoken': ['E9Zdag29N5T2CWw4yW4qbbD2S55gwCzc19Jv4UEiiYKCA0Cf4bsnF0RFHlCgQz3E'], 'groceryitem': ['dirt']}>
    data = request.POST
    # print('data', data)
    # hard_coded_item = 'catfoods'
    new_grocery_item = GroceryItem.objects.create(grocery_item_text=data['groceryitem'])
    return HttpResponseRedirect(reverse('grocery_list_app:grocerylist'))

def complete(request, item_id):
    #incomplete to complete
    print('item_id', item_id)
    item = get_object_or_404(GroceryItem, pk=item_id)
    print(item) #Apples
    return HttpResponseRedirect(reverse('grocery_list_app:grocerylist'))

# def incomplete(request):
    #complete to incomplete
    #item = 




# def complete(request):
# item = get_object_or_404(GroceryItem.objects.filter())