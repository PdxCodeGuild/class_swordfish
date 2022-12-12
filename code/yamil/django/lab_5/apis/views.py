from rest_framework import generics

from pokemon import models
from .serializers import PokemonSerializer, TypeSerializer

class ListPokemon(generics.ListCreateAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer
class ListType(generics.ListCreateAPIView):
    queryset = models.Type.objects.all()
    serializer_class = TypeSerializer