from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Url



def index(request):
    url_items = Url.objects.all()
    context = {
        'url_items': url_items,
    }
    return render(request, 'url_shortener_app/home.html', context)
    # return HttpResponse('Page Working')

def add(request):
    description = request.POST["long_text"]
    Url.objects.create(long_text=description)

    return HttpResponseRedirect(reverse('url_shortener_app:index'))