from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ChirpApp

class ChirpListView(ListView):
    model = ChirpApp
    template_name = 'home.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = ChirpApp
    template_name = 'create.html'
    fields = ['chirp']
    success_url = reverse_lazy('chirp:home')

    def form_valid(self, form):
        form.instance.chirper = self.request.user
        return super().form_valid(form)
