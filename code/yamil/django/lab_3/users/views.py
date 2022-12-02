from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # redirect to a success page
    # else:
    #     # return an 'invalid login' error message
