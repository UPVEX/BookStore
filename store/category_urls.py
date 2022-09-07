from django.urls import path

from .views import CategorysListView, CategoryDetail

urlpatterns = [
    path('', CategorysListView.as_view()),
    path('<int:category_id>/', CategoryDetail.as_view()),
]