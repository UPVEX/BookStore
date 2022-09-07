from django.urls import path

from .views import WriterListView, WriterDetail

urlpatterns = [
    path('', WriterListView.as_view()),
    path('<int:writer_id>/', WriterDetail.as_view()),
]
