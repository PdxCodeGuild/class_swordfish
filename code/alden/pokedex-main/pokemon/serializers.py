from rest_framework import serializers
from .models import Pokemon, Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['type']

class PokemonSerializer(serializers.ModelSerializer):
    types = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Pokemon
        fields = ('name', 'number', 'id', 'height', 'weight', 'image_front', 'image_back', 'types')