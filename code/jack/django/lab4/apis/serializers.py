from rest_framework import serializers
from students_app import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = models.Student