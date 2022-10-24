from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse 
from django.utils import timezone
from.models import GroceryItem


def index(request):
    incomplete = GroceryItem.objects.filter(task_completed=False).order_by('-created_date')
    complete = GroceryItem.objects.filter(task_completed=True).order_by('-completed_date')
    context = {
        'incomplete':incomplete,
        'complete':complete,
        }
    return render(request, 'grocery/index.html', context=context)

def add(request):
    # if request.method == 'POST':
    print(request.POST)
    new_item = GroceryItem.objects.create(description=request.POST['item'])
    print(new_item)
    return HttpResponseRedirect(reverse('grocery:index')) #standard practice to redirect when POST
    # return render(request, 'grocery/index.html', {'form': form})

def complete(request, pk):
    selected_item = get_object_or_404(GroceryItem, pk=pk)
    print(selected_item)
    selected_item.task_completed = True
    selected_item.completed_date = timezone.now()
    selected_item.save()
    # return render(request, 'grocery:index', completed_item=completed_item)
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    want_delete = get_object_or_404(GroceryItem, pk=pk)
    want_delete.delete()
    return HttpResponseRedirect(reverse('grocery:index'))