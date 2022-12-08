from django.contrib.auth.models import User, Group
from rest_framework import serializers

# could this be from users import models? and it would import all of them?
from users.models import CustomUser
from pokemon.models import Pokemon, Type


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "__all__"
            # this could be something like fields = ['url', 'username', 'email', 'groups']
        )


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = (
            "__all__"
        )


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            "__all__"
        )
