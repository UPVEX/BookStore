from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Writer, Book
from .serializers import categoryserializer, writerserializer, bookserializer

class BookListView(APIView):
    def get(self, request):
        b = Book.objects.all()
        serializer = bookserializer(b, many=True)
        return Response(serializer.data)

class CategoryListView(APIView):
    def get(self, request):
        c = Category.objects.all()
        serializer = categoryserializer(c, many=True)
        return Response(serializer.data)
