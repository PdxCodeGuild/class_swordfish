from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = [ 
            "number", 
            "name", 
            "height",
            "weight",
            ]
