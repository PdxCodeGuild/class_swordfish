from rest_framework import serializers
from students import models

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'favorite_teacher',
            'cohort',
            'favorite_topic',
            'favorite_teacher',
            'capstone',
        )
        model = models.Students