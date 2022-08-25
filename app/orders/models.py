from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product, SizeClothes

# todo add auto sum calculation

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='prod_in_cart', blank=True)
    sum = models.DecimalField(max_digits=6, decimal_places=2)


class CartProductsM2M(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    prod_clothes_size = models.CharField(max_length=50, choices=SizeClothes.Sizes.choices, blank=True, null=True)
    prod_foot_size = models.DecimalField(max_digits=3, decimal_places=1)
    amount = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Product"
