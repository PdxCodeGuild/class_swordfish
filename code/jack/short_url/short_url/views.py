from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import random, string
from datetime import datetime

from .models import Url, Click

def index(request):
    if request.method == 'POST':
        # all possible characters in code
        chars = string.ascii_letters + string.digits
        url = request.POST['url']

        # # no http breaks code - adds if missing
        # if 'http' not in url: 
        #     url = 'http://' + url

        code = ''.join([random.choice(chars) for _ in range(6)])

        creation_ip = request.META.get('REMOTE_ADDR')

        # create and save object
        link = Url(url=url, code=code, creation_ip=creation_ip, clicks=0)     
        link.save()

        return render(request, 'short_url/index.html', {'link':link})
    
    return render(request, 'short_url/index.html')


def redirect(request, code):
    url_object = get_object_or_404(Url.objects.filter(code=code))
    url = url_object.url

    # update Url data
    url_object.clicks = int(url_object.clicks) + 1
    url_object.save()

    # create Click data
    click = Click(client_ip=request.META.get('REMOTE_ADDR'), url=url_object)
    click.save()
    
    return HttpResponseRedirect(url)
