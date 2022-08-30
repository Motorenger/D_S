from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
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
