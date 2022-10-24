from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse 
from.models import GroceryItem
from .forms import CreateForm

def index(request):
    incomplete = GroceryItem.objects.filter(task_completed=False).order_by('-created_date')
    complete = GroceryItem.objects.filter(task_completed=True).order_by('-completed_date')
    context = {
        'incomplete':incomplete,
        'complete':complete,
        }
    return render(request, 'grocery/index.html', context=context)

def add(request):
    # item = GroceryItem.objects.all()
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
        # return HttpResponseRedirect(reverse('grocery:index', args=(form.id,))) #standard practice to redirect when POST
        return render(request, 'grocery/index.html', {'form': form})

def update(request):
    return HttpResponse(f'Which item would you like to update?')

def delete(request):
    return HttpResponse(f'Which item would you like to delete?')