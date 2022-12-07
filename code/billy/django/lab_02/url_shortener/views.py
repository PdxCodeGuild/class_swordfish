from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import UrlShortener
import random
import string

def index(request):
    urls = UrlShortener.objects.all()
    context = {
        'urls': urls
    }
    return render(request, 'url_shortener/index.html', context)

def shorten(request):
    print(request.POST)
    long_url = request.POST['long_url']
    print(long_url)
    code = ''
    for i in range(6):
        code += random.choice(string.ascii_letters + string.digits)
    print(code)
    shortened_url = UrlShortener(code=code, url=long_url)
    shortened_url.save()
    return HttpResponseRedirect(reverse('url_shortener:index'))


def redirect(request, code):
    shortened_url = get_object_or_404(UrlShortener, code=code)
    shortened_url.clicks += 1
    shortened_url.save()
    return HttpResponseRedirect(shortened_url.url)