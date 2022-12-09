from rest_framework import serializers
from pokemon.models import Pokemon
from pokemon.models import Type


class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            'type',
        )
class PokemonSerializer(serializers.ModelSerializer):
    # types = serializers.StringRelatedField(many=True)
    type_detail = NestedTypeSerializer(read_only=True, many=True, source='types')

    class Meta:
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_detail')
        model = Pokemon
# For each pokemon object, types should be fetched from database
the_type = Pokemon.objects.all()
# print(the_type)
    