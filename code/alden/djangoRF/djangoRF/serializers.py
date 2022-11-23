from rest_framework import serializers
from .models import StudentList

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = StudentList