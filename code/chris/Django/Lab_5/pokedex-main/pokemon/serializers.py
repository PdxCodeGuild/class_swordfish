# Serializers will take Django object(s) and convert to JSON data
from rest_framework import serializers
from .models import Pokemon
from .models import Type

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields =['name']

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = Pokemon
    
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = Type