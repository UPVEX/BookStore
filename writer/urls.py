from django.urls import path

from .views import WriterView

urlpatterns = [
    path('', WriterView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:book_id>/', WriterView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]

"""
from .views import WriterListView, WriterDetail

urlpatterns = [
    path('', WriterListView.as_view()),
    path('<int:writer_id>/', WriterDetail.as_view()),
]
"""