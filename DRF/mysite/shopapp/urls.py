from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (
    ShopIndexView,
    ProductDetailsView,
    ProductsListView,
    OrdersListView,
    OrderDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsDataExportView,
    ProductViewSet,
    OrderViewSet,
)

app_name = "shopapp"

# DRF API router
router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='api-products')
router.register(r'orders', OrderViewSet, basename='api-orders')

urlpatterns = [
    # HTML Views
    path("", ShopIndexView.as_view(), name="index"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/export/", ProductsDataExportView.as_view(), name="products-export"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/archive/", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
    path('blog/', include('blogapp.urls')),
    # API Routes
    path("api/", include(router.urls)),
]
