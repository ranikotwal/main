from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework . response import Response
from rest_framework import status
#from django.shortcuts import get_object_or_404

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

    