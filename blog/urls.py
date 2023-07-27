from django.urls import path
from .import views
from .views import CategoryListAPIView, CategoryDetailApiView, PostListAPIView, PostDetailApiView, ImageListAPIView, ImageDetailApiView


urlpatterns = [
    path("category/", CategoryListAPIView.as_view(), name="category-list-api"), 
    path('category/<int:pk>', CategoryDetailApiView.as_view()),

    #for posts
    path('post/', PostListAPIView.as_view(), name='post-list-api'),
    path('post/<int:pk>', PostDetailApiView.as_view()),

    #for image
    path('image/', ImageListAPIView.as_view(), name='image-list-api'),
    path('image/<int:pk>', ImageDetailApiView.as_view()),
]