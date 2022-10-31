from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from chirp.models import Chirp

class ChirpListView(ListView):
    model = Chirp
    template_name = 'index.html'

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'chirp_detail.html'

class ChirpCreateView(CreateView):
    model = Chirp
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']