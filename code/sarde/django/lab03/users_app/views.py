from django.shortcuts import render
from django.http import HttpResponse


def greeting(request):
    greeting = 'Hi'
    return HttpResponse(greeting)
