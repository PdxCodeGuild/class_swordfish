from django.shortcuts import render, get_object_or_404
from .models import GroceryItem
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

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

def complete(request, item_id):
    item = get_object_or_404(GroceryItem,pk=item_id)
    item.item_completed = True
    item.date_completed = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('my_grocery_list:list_view'))

def delete(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.item_deleted = True
    item.save()
    return HttpResponseRedirect(reverse('my_grocery_list:list_view'))

