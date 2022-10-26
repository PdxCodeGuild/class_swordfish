from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.utils import timezone
from .models import GroceryItems 

def index(request):
    return render()
