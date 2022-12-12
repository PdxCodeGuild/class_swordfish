from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Chirp

def index():
    return HttpResponse('OK')



class ChirpListView(ListView):
    model = Chirp
    template_name = 'home.html'

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'posts/detail.html'

class ChirpCreateView(CreateView):
    model = Chirp
    template_name = 'posts/new.html'
    fields = ['tiny_body']

    def form_valid(self, form):
        print()
        # print('form.instance.author', form.instance.author)
        print('self.request.user', self.request.user)
        print()
        form.instance.author = self.request.user
        return super().form_valid(form)

