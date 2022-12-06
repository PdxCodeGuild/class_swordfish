from django.shortcuts import render
from rest_framework import generics, viewsets

from pokemon import models
from .serializers import PokemonSerializer, TypeSerializer

# class ListPokemon(generics.ListCreateAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

# class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = TypeSerializer