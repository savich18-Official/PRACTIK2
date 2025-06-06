from django.urls import path
from .views import (
    shop_index, groups_list, products_list, orders_list,
    create_product, create_order,
)

urlpatterns = [
    path('', shop_index, name='shop_index'),
    path('groups/', groups_list, name='groups_list'),
    path('products/', products_list, name='products_list'),
    path('orders/', orders_list, name='orders_list'),
    path('products/create/', create_product, name='create_product'),
    path('orders/create/', create_order, name='create_order'),
]
