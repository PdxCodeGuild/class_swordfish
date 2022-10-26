from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import random
from .models import URLApp

def index(request):
    return render(request, 'url_app/index.html')

def add(request):
    url= request.POST.get('url_in_template')
    print(url)
    
    