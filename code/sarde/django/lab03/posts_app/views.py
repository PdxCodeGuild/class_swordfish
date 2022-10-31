from django.shortcuts import render
from django.http import HttpResponse


def greeting(request):
    greeting = 'Hi'
    return HttpResponse(greeting)

# ability to post chirps of some constrained length(e.g 128 characters)
# public profile page that shows all the users chirps
