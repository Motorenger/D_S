from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product, SizeClothes, SizeFoot


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product, through="CartProductsM2M", related_name='prod_in_cart', blank=True)
    sum = models.DecimalField(max_digits=6, decimal_places=2)

class CartProductsM2M(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products_m2m')
    prod_clothes_size = models.CharField(max_length=50, choices=SizeClothes.Sizes.choices, blank=True, null=True)
    prod_foot_size = models.ForeignKey(SizeFoot, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Product"


class Order(Cart):
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sum}, {self.date.strftime("%Y-%m-%d")}'
