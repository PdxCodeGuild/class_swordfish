from django.shortcuts import render
from rest_framework import viewsets, generics


from .serializers import UserSerializer, PokemonSerializer, TypeSerializer
from users.models import CustomUser
from pokemon.models import Pokemon, Type


# Create your views here for the apis app
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
