from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Chirp

class BlogListView(ListView):
    model = Chirp
    template_name = 'index.html'
