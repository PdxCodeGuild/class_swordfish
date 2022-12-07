from rest_framework import serializers
from pokemon import models

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = models.Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = models.Type