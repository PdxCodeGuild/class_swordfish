from django.shortcuts import render
from rest_framework import generics, viewsets
from pokemon.models import Pokemon
from .serializers import PokemonSerializer



# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
