from django.shortcuts import render
from rest_framework import viewsets, generics


from .serializers import UserSerializer, PokemonSerializer, TypeSerializer
from users.models import CustomUser
# the below get_user_model method uses django to pull current user info
from django.contrib.auth import get_user_model
from pokemon.models import Pokemon, Type


# Create your views here for the apis app
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CurrentUserViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # print(self.request.user)
        return get_user_model().objects.all().filter(id=self.request.user.id)
    serializer_class = UserSerializer
