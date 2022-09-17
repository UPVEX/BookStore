from django.urls import path

from .views import BookView

urlpatterns = [
    path('', BookView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:book_id>/', BookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]



"""
from .views import BookListView, BookDetail

urlpatterns = [
    path('', BookListView.as_view()),
    path('<int:book_id>/', BookDetail.as_view()),
]
"""