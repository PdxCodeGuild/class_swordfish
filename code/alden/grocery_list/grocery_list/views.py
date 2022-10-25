from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from grocery_list.models import GroceryItem


def index(request):
    latest_grocery_list = GroceryItem.objects.filter(pub_date__lte = timezone.now()).order_by('pub_date')
    return render(request, "grocery_list/index.html", {'latest_grocery_list': latest_grocery_list})

def complete(request, item_id):
    item = get_object_or_404(GroceryItem.objects.filter(pk= item_id))
    # complete = item.get(pk=request.POST['groceryitem'])
    item.completed_check = True
    item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def incomplete(request, item_id):
    item = get_object_or_404(GroceryItem.objects.filter(pk= item_id))
    item.completed_check = False
    item.completed_date = None
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index')) 

def delete(request, item_id):
    item = get_object_or_404(GroceryItem.objects.filter(pk= item_id))
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def add(request):
    new_item = request.POST['new_item']
    if len(new_item) > 0:
        n_item = GroceryItem(item_text=new_item, pub_date = timezone.now(), completed_date = None, completed_check = False)
        n_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))
