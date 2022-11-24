from django.shortcuts import render
from rest_framework import viewsets
from .models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer