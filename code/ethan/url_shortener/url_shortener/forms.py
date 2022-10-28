from django.forms import ModelForm
from .models import Shortener

class ShortenerForm(ModelForm):
	class Meta:
		model = Shortener
		fields = '__all__'