from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='productlist'),
    path('<int:productId>/',views.ProductDetailAPIView.as_view(), name='productdetail'),
]