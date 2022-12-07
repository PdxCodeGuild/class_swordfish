from django.shortcuts import render
from rest_framework import generics, viewsets
from .forms import PokemonForm
from pokemon import models
from .serializers import PokemonSerializer, TypeSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = TypeSerializer

def createView(request):
    context = {}

    form = PokemonForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, 'create_view.html', context)