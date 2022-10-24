from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from grocery_list.models import GroceryItem


def index(request):
    latest_grocery_list = GroceryItem.objects.filter(pub_date__lte = timezone.now()).order_by('pub_date')
    return render(request, "grocery_list/index.html", {'latest_grocery_list': latest_grocery_list})

def complete(request, item_id):
    item = get_object_or_404(GroceryItem.objects.filter(pub_date__lte = timezone.now()), pk= item_id)
    complete = item.get(pk=request.POST['complete_check'])
    return render 