from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import GroceryItem
from .forms import GroceryForm
from django.db import models


def index(request):
	grocery_list = GroceryItem.objects.all()
	form = GroceryForm()
	if request.method == 'POST':
		form = GroceryForm(request.POST)
		if form.is_valid():
			form.save()

	context = {"grocery_list": grocery_list, 'form': form}
	return render(request, 'index.html', context)

def complete(request, item_id):
	if request.method == 'POST':
		item = GroceryItem.objects.get(pk=item_id)
		item.complete = True
		item.complete_date = datetime.now()
		print(item.complete_date)
		item.save()
		return HttpResponseRedirect("../")

def delete(request, item_id):
	if request.method == 'POST':
		item = GroceryItem.objects.get(pk=item_id)
		item.delete()
		return HttpResponseRedirect("../")
