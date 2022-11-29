from django.shortcuts import render

from .models import GroceryItem


def index(request):
    complete_items = GroceryItem.objects.filter(completed=True)
    incomplete_items = GroceryItem.objects.filter(completed=False)
    context= {
        'complete_items' : complete_items,
        'incomplete_items' : incomplete_items,
        }
    return render(request, 'index.html', context)