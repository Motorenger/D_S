from rest_framework.decorators import api_view 
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view()
def poducts_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    
@api_view()
def poduct_detail(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)

        return Response(serializer.data)
        