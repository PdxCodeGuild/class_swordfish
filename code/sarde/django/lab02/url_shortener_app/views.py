from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import url_shortener_app
from .models import UrlShortener
import string
import random

# utility function/helper function


def generate_random_code():
    length_of_random_code = 6
    random_code = ''.join(random.choices(
        string.ascii_letters, k=length_of_random_code))
    print('random_code', random_code)
    return random_code


def greeting(request):
    greeting = 'Hi'
    return HttpResponse(greeting)


def index(request):
    url_shortener_objects = UrlShortener.objects.all()
    return render(request, 'url_shortener_app/url.html', {'url_shortener_objects': url_shortener_objects})


def create(request):
    user_input_url = request.POST.get('url')
    print('The URL the user entered', user_input_url)
    print('The keys', request.POST.keys())
    short_code = generate_random_code()
    url_shortener_object = UrlShortener.objects.create(
        input_url=user_input_url, short_code=short_code)
    print(url_shortener_object)
    return HttpResponseRedirect(reverse('url_shortener_app:index'))


def redirect(request, short_code):
    url_shortener_object = UrlShortener.objects.get(short_code=short_code)
    print(url_shortener_object)

    return HttpResponseRedirect(url_shortener_object.input_url)

    # https://www.google.com/
