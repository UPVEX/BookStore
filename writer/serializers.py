from rest_framework import serializers
from .models import Writer

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['name', 'updated_at']
