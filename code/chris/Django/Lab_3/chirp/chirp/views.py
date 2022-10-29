from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import ChirpApp

class ChirpListView(ListView):
    model = ChirpApp
    template_name = 'home.html'

class ChirpCreateView(CreateView):
    model = ChirpApp
    template_name = 'create.html'
    fields = ['chirp', 'chirper']