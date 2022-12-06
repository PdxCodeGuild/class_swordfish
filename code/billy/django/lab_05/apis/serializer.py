from rest_framework import serializers
from pokemon.models import Pokemon, Type
class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            # 'id',
            'type',
            # 'pokemon',
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


# class TypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Type
#         fields = ('__all__')
# class PokemonSerializer(serializers.ModelSerializer):
#     type = TypeSerializer(many=True)
#     class Meta:
#         model = Pokemon
#         fields = ('__all__')

#     def create(self, validated_data):
#         pokemon_type = validated_data.pop('types')
#         pokemon = Pokemon.objects.create(**validated_data)
#         for type in pokemon_type:
#             Type.objects.create(pokemon=pokemon, **type)
#         return pokemon