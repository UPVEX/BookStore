from rest_framework import viewsets

from .models import Writer
from .serializers import WriterSerializer


class WriterView(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer






"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status



from .models import Writer
from .serializers import WriterSerializer


class WriterListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        writers = Writer.objects.all()
        serializer = WriterSerializer(writers, many=True)
        return Response(serializer.data)

class WriterDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, writer_id):
        try:
            writer = Writer.objects.get(pk=writer_id)
        except Writer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WriterSerializer(writer)
        return Response(serializer.data)
"""