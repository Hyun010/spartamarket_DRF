from rest_framework import serializers
from .models import Product
from accounts.serializers import profileSerializer

class ProductSerializer(serializers.ModelSerializer):
    user = profileSerializer(read_only=True)
    class Meta :
        model = Product
        fields = '__all__'