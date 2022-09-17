from django.urls import path

from .views import CategoryView

urlpatterns = [
    path('', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:book_id>/', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]