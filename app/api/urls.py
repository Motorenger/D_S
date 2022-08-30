from django.urls import path

from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, CartList


urlpatterns = [
    path('products/list', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view(), name="product-detail"),

    path('categories/list', CategoryList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view(), name="category-detail"),

    path('carts/list', CartList.as_view()),
]
