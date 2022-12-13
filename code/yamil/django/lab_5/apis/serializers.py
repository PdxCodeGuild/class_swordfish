from rest_framework import serializers
from pokemon.models import Pokemon, Type
class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            'type',
        )

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(read_only=True, many=True, source='types')
    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'type_detail',
            )
        model = Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Type
