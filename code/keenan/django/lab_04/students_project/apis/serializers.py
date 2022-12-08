from rest_framework import serializers
from students_app import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            # this could be a list of each data field for our model
            # individually, or we can use the dunder string below
            "__all__"
        )
        model = models.Student
        