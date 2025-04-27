from django.shortcuts import render
from shopapp.models import Product, Order  # Импортируем нужные модели

# Функция для отображения списка продуктов
def product_list(request):
    products = Product.objects.all()  # Получаем все продукты
    return render(request, 'shopapp/product_list.html', {'products': products})

# Функция для отображения списка заказов
def order_list(request):
    orders = Order.objects.all()  # Получаем все заказы
    return render(request, 'shopapp/order_list.html', {'orders': orders})
