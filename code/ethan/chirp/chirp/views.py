from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from chirp.models import Chirp
from django.urls import reverse_lazy

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

class ChirpEditView(UpdateView):
    model = Chirp
    template_name = 'edit_post.html'
    fields = ['title', 'body']

class ChirptDeleteView(DeleteView):
    model = Chirp
    template_name = 'delete_post.html'
    success_url = reverse_lazy('chirp:index')