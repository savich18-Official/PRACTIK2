from django.urls import path
from . import views  # Убедись, что ты правильно импортировал views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # Это должно работать
    path('orders/', views.order_list, name='order_list'),
]
