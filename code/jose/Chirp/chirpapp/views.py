from django.shortcuts import render
from django.views.generic import ListView
from time import timezone
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from . models import Chirps
# Create your views here.
from django.http import HttpResponse
def index(request):
    chirps = Chirps.objects.all()
    context = {
        'chirp_list': chirps
    }
    return render(request, 'index.html', context)
    return HttpResponse('ok')

def newchirp(request):
    if request.user.is_authenticated == True:
        chirps = request.POST['post']
        Chirps.objects.create(chirp = chirps, chirper = request.user)
        return HttpResponseRedirect(reverse('chirps:index'))
    else:
        return HttpResponseRedirect(reverse('login'))