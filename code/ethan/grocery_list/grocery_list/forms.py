from django.forms import ModelForm
from .models import GroceryItem

class GroceryForm(ModelForm):
	class Meta:
		model = GroceryItem
		fields = '__all__'