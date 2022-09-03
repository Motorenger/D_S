from rest_framework import serializers 

from .models import Cart, CartProductsM2M
from products.models import Product





class CartProductsSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Product
        fields = ["id"]


class CartProductsM2MSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProductsM2M
        exclude = ["cart"]
        


class CartSerializer(serializers.ModelSerializer):
    products = CartProductsM2MSerializer(many=True, source='cart_products_m2m', read_only=True)

    class Meta: 
        model = Cart
        fields = ["id", "user", "sum", "products"]


class CartProductsM2MSerializerAdd(serializers.ModelSerializer):
    '''
     Serializer for adding products to cart
    '''
    class Meta:
        model = CartProductsM2M
        exclude = ["product", "cart"]