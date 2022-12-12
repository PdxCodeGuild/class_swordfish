from pokedex_app.models import Pokemon, Type
from rest_framework import serializers

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('__all__')

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'weight', 'height', 'image', 'type')