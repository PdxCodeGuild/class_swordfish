
from django.urls import reverse
from rest_framework import generics 
from pokedex_app import models
from . serializer import PokemonSerializer, TypeSerializer

class ListPokemon(generics.ListCreateAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class ListType(generics.ListCreateAPIView):
    queryset = models.Type.objects.all()
    serializer_class = TypeSerializer
class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer