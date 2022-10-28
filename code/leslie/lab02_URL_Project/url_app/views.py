from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import random
import string
from django.urls import reverse
from .models import UrlApp

def index(request):
    all_urls = UrlApp.objects.all()
    context = { 
        'all_urls': all_urls
    }
    return render(request, 'url_app/index.html', context=context)

def shorten_url(request):
    if request.method == 'POST':
        url=request.POST["shorten_url"]
        new_url = UrlApp(url=url, short_url=generate_random())
        new_url.save()
        return HttpResponseRedirect('/')

def generate_random():
        short_url = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(6))
        return short_url
    

                            
                        


    