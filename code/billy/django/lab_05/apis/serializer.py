from rest_framework import serializers
from pokemon.models import Pokemon, Type

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Type