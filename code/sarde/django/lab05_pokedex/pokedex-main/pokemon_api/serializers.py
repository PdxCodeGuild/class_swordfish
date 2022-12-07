from rest_framework import serializers
from pokemon.models import Pokemon
from pokemon.models import Type

class PokemonSerializer(serializers.ModelSerializer):
    types = serializers.StringRelatedField(many=True)


    class Meta:
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'types')
        model = Pokemon
# For each pokemon object, types should be fetched from database
the_type = Pokemon.objects.all()
# print(the_type)
    