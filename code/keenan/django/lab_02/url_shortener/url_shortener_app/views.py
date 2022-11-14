from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Url

import random
import string

# create two views, one that will generate a random shortened_code
# a second view to check that and then redirect the user to the long url if it was in the db

def index(request):
    # we don't need context or to display anything here, later, this is to show our db during development
    url_items = Url.objects.all()
    context = {
         'url_items': url_items,
    }
    return render(request, 'url_shortener_app/home.html', context)


def add(request):
    random_code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    description = request.POST["long_text"]
    item = Url.objects.create(long_text=description, shortened_code=random_code)
    item.save()
    return HttpResponseRedirect(reverse('url_shortener_app:index'))

#  currently no check to see if the item already has a code associated with it. could reassign a new code if there was one already?