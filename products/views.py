from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProductListAPIView(APIView):
    @permission_classes(IsAuthenticated)
    @authentication_classes([JWTAuthentication])
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @permission_classes([AllowAny])
    def get(self, request):
        products = Product.objects.all()
        paginator = PageNumberPagination()
        page_size=request.GET.get('size')
        if not page_size==None:
            paginator.page_size = page_size
        result = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
