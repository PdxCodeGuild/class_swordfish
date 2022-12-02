from .models import Students
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Students