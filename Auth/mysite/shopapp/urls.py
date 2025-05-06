from django.urls import path
from shop.views.products import (
    ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductArchiveView
)
from shop.views.orders import (
    OrderListView, OrderDetailView, OrderCreateView,
    OrderUpdateView, OrderDeleteView
)

urlpatterns = [
    # Продукты
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/archive/', ProductArchiveView.as_view(), name='product_archive'),

    # Заказы
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]
