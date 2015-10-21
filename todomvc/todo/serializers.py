from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'completed', 'order']
