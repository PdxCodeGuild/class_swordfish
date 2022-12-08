from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from . models import Url
from random import choice
from string import ascii_letters, digits


def index(request):

    url2 = Url()
    form = request.POST

    if request.method == 'POST':
        url2.long = form.get('long_url')
        url2.short = ''.join([choice(ascii_letters + digits)for i in range(6)])
        url2.save()
        context = {
            'results': Url.objects.all()
        }
        return render(request, 'url_app/index.html', context)
    else:
        context = {
            'results': Url.objects.all()
        }
        return render(request, 'url_app/index.html', context)
   


def submit(request):
    return HttpResponse(''.join([choice(ascii_letters + digits)for i in range(6)]))


def redirect(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    return HttpResponse(url.long)
