from django.urls import path
from .import views
from .views import CategoryListAPIView


urlpatterns = [
    path("category/", CategoryListAPIView.as_view(), name="category-list-api"), 
]