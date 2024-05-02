from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
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

class ProductDetailAPIView(APIView):
    def get_object(self, productId):
        return get_object_or_404(Product, pk=productId)

    def put(self, request,productId):
        product=self.get_object(productId)
        if request.user==product.user:
            serializer = ProductSerializer(product,data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message":"잘못된 접근입니다."},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,productId):
        product=self.get_object(productId)
        if request.user==product.user:
            product.delete()
            return Response({"message":"삭제되었습니다."},status=status.HTTP_200_OK)
        else:
            return Response({"message":"잘못된 접근입니다."},status=status.HTTP_400_BAD_REQUEST)