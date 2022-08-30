from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product, Category
from products.serializers import ProductSerializer, CategotySerializer


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

    def get_product(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        product = self.get_product(pk)
        serializer = CategotySerializer(product, context={'request': request})

        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_product(pk)
        serializer = CategotySerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
