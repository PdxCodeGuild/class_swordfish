
from rest_framework import serializers
from .models import Todo

# Serializers convert Django objects into JSON data


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify fields individually 
        # fields = ("title", "description", "created_at", "completed", "id")
        # Or use the __all__ to include all fields
        fields = ("__all__")
        model = Todo