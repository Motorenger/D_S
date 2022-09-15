from rest_framework import serializers

from .models import Product, Category, Brand


class BrandSerializer(serializers.Serializer):

    class Meta:
        model = Brand
        fields = ['id', 'name',]

class ProductSerializer(serializers.ModelSerializer):
    
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

class CategotySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product_detail'
    )

    class Meta:
        model = Category
        fields = "__all__"
