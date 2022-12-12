from rest_framework import serializers
from . models import Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model: Students