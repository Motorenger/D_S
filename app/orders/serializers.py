from rest_framework import serializers 

from .models import Cart, CartProductsM2M
from products.models import Product




class CartProductsSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta: 
        model = Product
        fields = ["url", "name", "description", "price", "brand"]


class CartProductsM2MSerializer(serializers.ModelSerializer):
    product = CartProductsSerializer()

    class Meta:
        model = CartProductsM2M
        fields = ["product", "prod_clothes_size", "prod_foot_size", "amount"]
        


class CartSerializer(serializers.ModelSerializer):
    products = CartProductsM2MSerializer(many=True, source='cart_products_m2m')

    class Meta: 
        model = Cart
        fields = ["id", "sum", "products"]
