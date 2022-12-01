import datetime
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
    # data <QueryDict: {'csrfmiddlewaretoken': ['E9Zdag29N5T2CWw4yW4qbbD2S55gwCzc19Jv4UEiiYKCA0Cf4bsnF0RFHlCgQz3E'], 'groceryitem': ['dirt']}>
    data = request.POST
    # print('data', data)
    # hard_coded_item = 'catfoods'
    new_grocery_item = GroceryItem.objects.create(
        grocery_item_text=data['groceryitem'])
    return HttpResponseRedirect(reverse('grocery_list_app:grocerylist'))


def complete(request, item_id):
    # print('item_id', item_id)
    item = get_object_or_404(GroceryItem, pk=item_id)
    # print(item) #Apples
    # print('item completed', item.completed)
    item.completed = True
    item.completed_date = datetime.datetime.now()
    # print('item completed', item.completed)
    item.save()
    return HttpResponseRedirect(reverse('grocery_list_app:grocerylist'))


def incomplete(request, item_id):
    print('item_id', item_id)
    item = get_object_or_404(GroceryItem, pk=item_id)
    # print(item) #Apples
    # print('item incomplete', item.completed)
    item.completed = False
    item.completed_date = None
    # print('item incomplete')
    # print(f'item was completed on: {item.completed_date}')
    # print(f'item was completed on {item.completed_date}')
    item.save()
    return HttpResponseRedirect(reverse('grocery_list_app:grocerylist'))


def delete(request, item_id):
    # The view function will accept the grocery item id
    # and get the actual grocery item for that id from the database.
    item = get_object_or_404(GroceryItem, pk=item_id)
# The view function will then delete that grocery item from the database.
    deleted_item = GroceryItem.objects.filter(id=item_id).delete()
# The view function will then redirect user back to the home type list page.
    return HttpResponseRedirect(reverse('grocery_list_app:grocerylist'))
