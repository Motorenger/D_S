from django.contrib import admin

from .models import (Cart, CartProductsM2M, Order, OrderProductsM2M)
from .forms import CartForm


class CartProductsM2MInline(admin.TabularInline):
    model = CartProductsM2M
    extra = 1 


class CartAdmin(admin.ModelAdmin):
    form = CartForm
    inlines = [
        CartProductsM2MInline,
        ]


class OrderProductsM2MInline(admin.TabularInline):
    model = OrderProductsM2M
    extra = 1 

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderProductsM2MInline,
    ]


admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartProductsM2M)
