from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Pokemon
from rest_framework import routers, serializers, viewsets
from .serializers import PokemonSerializer, TypeSerializer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

# Create your views here.

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

def index(request):
    return render(request, 'index.html')

class PokemonCreateView(LoginRequiredMixin, CreateView):
    model = Pokemon
    template_name = 'new_pokemon.html'
    fields = ['number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by']

def edit(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'edit_pokemon.html', {'pokemon': pokemon})
