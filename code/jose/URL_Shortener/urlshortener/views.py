from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import  reverse
from . models import URL_Shortener
import string, random

def index(request):
    urls = URL_Shortener.objects.all()
    context ={ 'urls': urls}
    return render(request, 'index.html', context)

def returnshorturl(request):
    userurl = request.POST.get('url', False)
    newurl = ''.join(random.choice(string.ascii_uppercase+string.digits)for _ in range(6))
    shortenedurl = URL_Shortener(original_url = userurl,new_url=newurl)
    shortenedurl.save()
    return HttpResponseRedirect(reverse('urlshortener:index'))

# Create your views here.
