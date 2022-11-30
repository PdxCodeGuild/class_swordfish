from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("Hello World!")

def submit_url(request):
    return HttpResponse("Hello World!")

def url_redirect(request):
    return HttpResponseRedirect("index/")