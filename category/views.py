from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer







"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .models import Category
from .serializers import CategorySerializer

class CategorysListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)
class CategoryDetail(APIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)
        return Response(serializer.data)
"""