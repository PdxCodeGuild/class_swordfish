from django.shortcuts import render
from .models import GroceryItem
from django.http import HttpResponseRedirect
from django.urls import reverse

def add(request):
    data = request.POST
    print('form data: ', data)
    item = data['item']
    print(item)
    new_grocery_item = GroceryItem.objects.create(item_description=item)
    print(new_grocery_item)
    return HttpResponseRedirect(reverse('my_grocery_list:list_view'))


def my_list(request):
    items = GroceryItem.objects.all()
    return render(request, 'my_grocery_list/my_list.html', {'items': items})
