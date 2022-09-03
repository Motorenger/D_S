from django.contrib import admin

from .models import (Product, Brand, Category, ProdPickture, SizeClothes, SizeFoot, SizeClothesM2M)
from .froms import CategoryForm


class SizeClothesInline(admin.TabularInline): 
    model = SizeClothesM2M
    extra = 6


class ProdPicktureInline(admin.TabularInline):
    model = ProdPickture 


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        SizeClothesInline,
        ProdPicktureInline
        ]


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ("name", "slug")


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(SizeFoot)
