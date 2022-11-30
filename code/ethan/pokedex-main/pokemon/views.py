from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
from rest_framework import routers, serializers, viewsets
from .serializers import PokemonSerializer, TypeSerializer
# Create your views here.
def index(request):
    return HttpResponse('ok')

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer