from django.forms import ModelForm
from .models import GroceryItem

class CreateForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['description']