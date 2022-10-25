from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import random, string

from .models import Url

def index(request):
    if request.method == 'POST':
        # all possible characters in code
        chars = string.ascii_letters + string.digits
        url = request.POST['url']

        # # no http breaks code - adds if missing
        # if 'http' not in url: 
        #     url = 'http://' + url

        code = ''.join([random.choice(chars) for _ in range(6)])
        
        # create and save object
        link = Url(url=url, code=code)
        link.save()

        return render(request, 'short_url/index.html', {'link':link})
    
    return render(request, 'short_url/index.html')


def redirect(request, code):
    x = get_object_or_404(Url.objects.filter(code=code))
    url = x.url
    return HttpResponseRedirect(url)
