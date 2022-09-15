from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404

from products.models import Product, Category
from products.serializers import ProductSerializer, CategotySerializer

from orders.models import Cart, CartProductsM2M
from orders.serializers import (CartSerializer, CartProductsM2MSerializerAdd, 
                                OrderSerializer)

from users.models import CustomUser


class ProductList(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serizializer = ProductSerializer(data=request.data)
        if serizializer.is_valid():
            serizializer.save()

            return Response(serizializer.data)
        else:
            return Response(serizializer.errors)

    
class ProductDetail(APIView):

    def get_product(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, context={'request': request})

        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartAddProdAPIView(generics.CreateAPIView):
    serializer_class = CartProductsM2MSerializerAdd


    def perform_create(self, serializer):
        
        product = Product.objects.get(pk=self.kwargs.get("pk"))
        cart = Cart.objects.get(user=self.request.user.pk)
        if serializer:
            serializer.save(product=product, cart=cart)
            cart.sum += serializer.validated_data["amount"] * product.price
            cart.save()



class CategoryList(APIView):
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategotySerializer(categories, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serizializer = CategotySerializer(data=request.data)
        if serizializer.is_valid():
            serizializer.save()

            return Response(serizializer.data)
        else:
            return Response(serizializer.errors)

class CategoryDetail(APIView):

    def get_category(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        category = self.get_category(pk)
        serializer = CategotySerializer(category, context={'request': request})

        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_category(pk)
        serializer = CategotySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartList(APIView):
    
    def get(self, request):
        categories = Cart.objects.all()
        serializer = CartSerializer(categories, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serizializer = CartSerializer(data=request.data)
        if serizializer.is_valid():
            serizializer.save()

            return Response(serizializer.data)
        else:
            return Response(serizializer.errors)


class CartDetail(APIView):

    def get_cart(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        cart = self.get_cart(pk)
        serializer = CartSerializer(cart, context={'request': request})

        return Response(serializer.data)

    def put(self, request, pk):
        cart = self.get_cart(pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaceOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer


    def perform_create(self, serializer):
        product = Product.objects.get(pk=1)
        user=CustomUser.objects.get(pk=self.request.user.pk)
        cart = Cart.objects.get(id=1)

        if serializer:
            serializer.save(sum=cart.sum, buyer=user, products=cart.products.all())
            print(serializer.data)
            print(cart.products.all())

