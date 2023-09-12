"""API serializers."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """TaskSerializer class."""

    class Meta:
        """Meta class."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
