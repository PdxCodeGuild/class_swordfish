import random
import string
from django import shortcuts

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse

from.models import CodeStorage

#CRUDL Time

def index(request):
    urls = CodeStorage.objects.all()
    context = {
        "urls":urls
    }
    # url_create = CodeStorage.objects.create(long_url=request.POST['url'])
    #i need to take in long url and save it to database
    return render(request, 'url_app/index.html', context=context)

def shortcode(request):
    short_url = generator()
    long_url = request.POST["long_url"]
    new_codestorage = CodeStorage.objects.create(long_url=long_url, short_url=short_url)
    new_codestorage.save()
    return HttpResponseRedirect(reverse('url_app:index'))

def generator():
    characters = string.ascii_letters + string.digits
    short_url_list = []  
    while len(short_url_list) < 6:
        short_url_list.append(random.choice(characters))
    short_string_url = "".join(short_url_list)
    return short_string_url

def redirect(request, pk):
    new_url = get_object_or_404(CodeStorage, pk=pk)
    # print(long_url)
    # print("------")
    # print(new_url.long_url)
    return HttpResponseRedirect(new_url.long_url)