from django.contrib.auth.models import User, Group
from rest_framework import serializers

# could this be from users import models? and it would import all of them?
from users.models import CustomUser
from pokemon.models import Pokemon, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            "__all__"
        )


class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = [
            'type',
        ]


class PokemonSerializer(serializers.ModelSerializer):
    nested_types = NestedTypeSerializer(source="types", many=True, read_only=True)

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'nested_types',
        ]


class UserSerializer(serializers.ModelSerializer):
    caught_list = PokemonSerializer(source='caught', many=True)
 
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'caught',
            'caught_list',
        )
