
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from django.core.paginator import Paginator

from .models import Category, Writer, Book
from .serializers import categoryserializer, writerserializer, bookserializer

#...................category...........................................

class CategorysListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        categorys = Category.objects.all()
        serializer = categoryserializer(categorys, many=True)
        return Response(serializer.data)
class CategoryDetail(APIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = categoryserializer(category)
        return Response(serializer.data)


#..........................book.....................................


class BookListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        books = Book.objects.all()
        serializer = categoryserializer(books, many=True)
        return Response(serializer.data)

class BookDetail(APIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = bookserializer(book)
        return Response(serializer.data)


#.....................writer.........................................
class WriterListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        writers = Writer.objects.all()
        serializer = writerserializer(writers, many=True)
        return Response(serializer.data)

class WriterDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, writer_id):
        try:
            writer = Writer.objects.get(pk=writer_id)
        except Writer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = writerserializer(writer)
        return Response(serializer.data)
