from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer
# Create your views here.

def index(request):
    return HttpResponse("ok")

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer