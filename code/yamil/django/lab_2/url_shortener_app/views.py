import random
import string
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . models import Url
from django.urls import reverse

def index(request):
    list_of_urls = Url.objects.all().order_by('-id')
    context = {
        'the_stuff' : list_of_urls
    }
    return render(request, 'index.html', context)

def submit_url(request):
    long_url = request.POST['long_url']
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for i in range(6))
    new_url = Url.objects.create(long_url=long_url, short_code=short_code)
    return HttpResponseRedirect(reverse('url_shortener:index'))

def url_redirect(request, code):
    print("Code is:", code)
    the_specific_url = get_object_or_404(Url, short_code=code)
    return HttpResponseRedirect(the_specific_url.long_url)

# https://www.google.com/
# http://localhost:8000/redirect/123xyz/
# http://localhost:8000/admin/url_shortener_app/url/