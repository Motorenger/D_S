from django.urls import path, include

from .views import (ProductList, ProductDetail, CategoryList,
                    CategoryDetail, CartList, CartDetail,
                    CartAddProdAPIView,
                    )


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('products/list', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view(), name="product-detail"),

    path('categories/list', CategoryList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view(), name="category-detail"),

    path('carts/list', CartList.as_view()),
    path('carts/<int:pk>', CartDetail.as_view(), name="cart-detail"),
    path('carts/add-to-cart/<int:pk>', CartAddProdAPIView.as_view()),

]
