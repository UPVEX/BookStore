from django.urls import path

from .views import BookListView, BookDetail

urlpatterns = [
    path('', BookListView.as_view()),
    path('<int:book_id>/', BookDetail.as_view()),
]