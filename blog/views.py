from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category, Post, Image
from .serializers import CategorySerializer, PostSerializer ,ImageSerializer
from rest_framework . response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class CategoryListAPIView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        if request.query_params:
            categorys = Category.objects.filter(**request.query_params.dict())
        else:
            categorys = Category.objects.all()

        if categorys:
            serializer = CategorySerializer(categorys, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **Kargs):
        '''
        post category data
        '''
        data = {}
        categorys = CategorySerializer(data = request.data)
        if categorys.is_valid():
            categorys.save()
            return Response(categorys.data)
        else:
            return  Response(status=status.HTTP_404_NOT_FOUND)


class CategoryDetailApiView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, pk=None):
        '''
        get single Category
        '''
        if pk:
            try:
                category = Category.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            if category:
                serializer = CategorySerializer(category)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        Update the Category
        '''
        category = Category.objects.get(pk=pk)
        data = CategorySerializer(instance =category , data= request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete category
        '''
        category = get_object_or_404(Category , pk=pk)
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class PostListAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request, *args, **Kwargs):
        queryset = Post.objects.all()
        if request.query_params:
            posts = Post.objects.filter(**request.query_params.dict())
        else:
            posts = Post.objects.all()

        if posts:
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self ,request, *args, **kargs):
        '''
        post data
        '''
        data = {}
        posts = PostSerializer(data = request.data)
        if posts.is_valid():
            posts.save()
            return Response(posts.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostDetailApiView(APIView):
    serializer_class = PostSerializer

    def get(self , request, pk= None):
        '''
        get single Post
        '''
        if pk:
            try:
                post = Post.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if post:
                serializer= PostSerializer(post)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(selt, request, pk=None):
        '''
        update post
        '''
        post = Post.objects.get(pk=pk)
        data = PostSerializer(instance= post , data= request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete Post
        '''
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ImageListAPIView(APIView):
    serializer_class= ImageSerializer

    def get(self, request, *args, **Kargs):
        queryset = Image.objects.all()
        if request.query_params:
            images= Images.objects.filter(**request.query_params.dict())
        else:
            images = Image.objects.all()
        if images:
            serializer = ImageSerializer(images, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request,*args, **kargs):
        '''post the image
        '''
        data = {}
        images= ImageSerializer(data= request.data)
        if images.is_valid():
            images.save()
            return Response(images.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ImageDetailApiView(APIView):
    serializer_class = ImageSerializer

    def get(self, request, pk=None):
        '''
        get single image
        '''
        if pk:
            try:
                image = Image.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if image:
                serializer = ImageSerializer(image)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        update image
        '''
        image = Image.objects.get(pk=pk)
        data= ImageSerializer(instance= image, data= request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete image
        '''
        image= get_object_or_404(Image, pk=pk)
        image.delete()
        return Response(status=status.HTTP_202_ACCEPTED)