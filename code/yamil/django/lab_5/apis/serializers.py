from rest_framework import serializers
from pokemon import models

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'number',
            'image_front'
        )
        model = models.Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'type',
        )
        model = models.Type