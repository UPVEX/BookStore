from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status



from .models import Book
from .serializers import BookSerializer



class BookListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookDetail(APIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data)

"""