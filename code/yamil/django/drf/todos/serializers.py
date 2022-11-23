from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ("title", "description", "created_at", "completed", "id")
        fields = ("__all__")
        model = Todo
