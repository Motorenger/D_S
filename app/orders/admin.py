from django.contrib import admin

from .models import (Cart, CartProductsM2M)
from .forms import CartForm


class CartProductsM2MInline(admin.TabularInline):
    model = CartProductsM2M
    extra = 1 


class CartAdmin(admin.ModelAdmin):
    form = CartForm
    inlines = [
        CartProductsM2MInline,
        ]



admin.site.register(Cart, CartAdmin)
