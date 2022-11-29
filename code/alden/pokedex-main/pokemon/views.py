from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

def profileview(request):
    return render(request, 'index.html')

def caughtPokemon(request, pokemon_id):
    pokelist = get_object_or_404(Pokemon, pk=pokemon_id)
    pokelist.caught_by.add(request.user)
    return render(request, 'index.html', {'pokelist': pokelist})

def releasedPokemon(request, pokemon_id):
    pokelist = get_object_or_404(Pokemon, pk=pokemon_id)
    pokelist.caught_by.remove(request.user)
    return render(request, 'index.html', {'pokelist': pokelist})