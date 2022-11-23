from rest_framework import serializers
from pokemon import models

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = ['type',]  

class PokemonSerializer(serializers.ModelSerializer):
    types = serializers.StringRelatedField(many=True, read_only=True)
    # types = TypeSerializer(many=True, read_only=True)
    class Meta:
        fields = ['number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'types',]
        model = models.Pokemon