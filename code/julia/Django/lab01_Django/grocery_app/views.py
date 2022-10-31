from binascii import Incomplete
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem

def basis(request):
    return HttpResponse('To Do List')
    
    #return render(request, 'grocery_app/basis.html', context)
   # Incompleted_items = GroceryItem.objects.filter(completed=False).order_by('date_created')


# Create your views here.
