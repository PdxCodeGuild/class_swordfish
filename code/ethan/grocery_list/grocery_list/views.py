from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GroceryItem
from .forms import GroceryForm


def index(request):
	grocery_list = GroceryItem.objects.all()
	form = GroceryForm()
	if request.method == 'POST':
		form = GroceryForm(request.POST)
		if form.is_valid():
			form.save()

	context = {"grocery_list": grocery_list, 'form': form}
	return render(request, 'index.html', context)

def completeItem(request, item_id):
	if request.method == 'POST':
		item = GroceryItem.objects.get(pk=item_id)
		item.complete = True
		item.save()

		return redirect('index')


def deleteItem(request, item_id):
	if request.method == 'POST':
		item = GroceryItem.objects.get(pk=item_id)
		item.delete()
		return redirect('index')
