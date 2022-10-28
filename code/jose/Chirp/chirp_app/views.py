from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

# Create your views here.

from . models import Chirp

class ChirpListView(ListView):
    model = Chirp
    template_name = 'chirp.html'
    

