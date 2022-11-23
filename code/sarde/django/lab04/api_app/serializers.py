from rest_framework import serializers
from students_app.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = Student
