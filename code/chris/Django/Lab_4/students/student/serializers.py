# Serializers will take Django object(s) and convert to JSON data
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ("first_name", "last_name", "cohort", "favorite_topic", "favorite_teacher", "capstone", "id")
        # OR
        fields = ("__all__")
        model = Student
