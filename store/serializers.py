from rest_framework import serializers
from .models import Category, Writer, Book

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'updated_at']

class writerserializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['name', 'updated_at']


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'writer', 'category', 'price', 'enable']
