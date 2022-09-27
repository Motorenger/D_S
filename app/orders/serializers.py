from rest_framework import serializers 

from .models import Cart, CartProductsM2M, Order
from products.models import Product
from products.serializers import ProductSerializer


class CartAndOrderProductsM2MSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(source='product.id')
    name = serializers.CharField(source='product.name')

    class Meta:
        model = CartProductsM2M
        exclude = ["cart"]
        


class CartSerializer(serializers.ModelSerializer):
    products = CartAndOrderProductsM2MSerializer(many=True, source='cart_products_m2m', read_only=True)

    class Meta: 
        model = Cart
        fields = ["id", "user", "sum", "products"]
    
    # todo add feature to update amount value thorugh cart detail  
    # def update(self, instance, validated_data):
    #     return instance
        


class CartProductsM2MSerializerAdd(serializers.ModelSerializer):
    '''
     Serializer for adding products to cart
    '''
    class Meta:
        model = CartProductsM2M
        exclude = ["product", "cart"]


class OrderSerializer(serializers.ModelSerializer):
    products = CartAndOrderProductsM2MSerializer(many=True, source='cart_products_m2m', read_only=True)
    
    def create(self, validated_data):
        products = validated_data.pop('products')
        cart = Cart.objects.get(user=validated_data['buyer'])
        order = Order.objects.create(**validated_data)
        print(cart.products.all())
        for product in cart.products.all():
            order.products.add(product)
        
        return order

    class Meta: 
        model = Order
        # fields = ["id", "user", "sum", "products", "approved", "date"]
        fields = ["id", "products", "approved"]