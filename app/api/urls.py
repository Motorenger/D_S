from django.urls import path

from .views import poducts_list, poduct_detail


urlpatterns = [
    path('products/list', poducts_list),
    path('products/detail/<int:id>', poduct_detail),
]
