from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

from . models import Chirp

class ChirpListView(ListView):
    model = Chirp
    template_name = 'chirp.html'

class ChirpCreateView(CreateView):
    model = Chirp
    template_name = 'chirp_create.html'
    fields = ['chirp', 'chirper']

    def form_valid(self, form):
        form.instance.chirper=self.request.user
        form.save()
        return super().form_valid(form)

class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chirp
    template_name = 'chirp_edit.html'
    fields = ['chirp']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = 'chirp_delete.html'
    success_url = reverse_lazy('chirp:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

