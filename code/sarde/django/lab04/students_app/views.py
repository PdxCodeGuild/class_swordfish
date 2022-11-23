from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# http://127.0.0.1:8000/students/greeting/


def greeting(request):
    greeting = 'Hello Students'
    return HttpResponse(greeting)
