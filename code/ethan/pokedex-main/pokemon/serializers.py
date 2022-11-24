from rest_framework import serializers
from .models import Pokemon, Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('__all__')

class PokemonSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True)

    class Meta:
        fields = ('__all__')
        model = Pokemon

    def create(self, validated_data):
        types_data = validated_data.pop('types')
        pokemon = Pokemon.objects.create(**validated_data)
        for type_data in types_data:
            Type.objects.create(pokemon=pokemon, **type_data)
        return pokemon