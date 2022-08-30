from rest_framework import serializers 

from .models import Cart, CartProductsM2M
from products.models import Product

class CartProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    products = CartProductsSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = "__all__"
