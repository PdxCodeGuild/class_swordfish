from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    # context = {}
    # return render(request, 'grocery_app/index.html', context)
    return HttpResponse("You are at the index.")

def about(request):
    return HttpResponse("You are at the about page.")