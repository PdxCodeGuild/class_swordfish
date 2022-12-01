from django.views.generic import ListView
from time import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

from . models import Chirp

def index(request):
    posts = Chirp.objects.all()
    context = {
        'chirp_list': posts
    }
    return render(request, 'home.html', context)

def new_post(request):
    if request.user.is_authenticated == True:
        posts = request.POST['chirp']
        Chirp.objects.create(post = posts, author = request.user)
        return HttpResponseRedirect(reverse('Chirp:index'))
    else:
        return HttpResponseRedirect(reverse('login'))

