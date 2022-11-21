import imp
import re
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from.models import Switch

import random
import string

def index(request):
    # url_list = Switch.objects
    return render(request, 'short/index.html')

def submit(request):
    new_url = request.POST['long_url']
    code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    if len(new_url) > 0:
        n_url = Switch(long_url = new_url, code = code)
        n_url.save()
    return render(request, 'short/index.html', {'n_url':n_url})
    
    
def code(request, code):
    redirect = get_object_or_404(Switch, code = code)
    url = redirect.long_url
    return HttpResponseRedirect(url)
