from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .models import Product, Order
from .forms import ProductForm, OrderForm  # импортируем формы


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999),
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


# ✅ Новая view-функция: создание продукта
def create_product(request: HttpRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')  # или на другой путь, если хочешь
    else:
        form = ProductForm()
    return render(request, 'shopapp/product_create.html', {'form': form})


# ✅ Новая view-функция: создание заказа
def create_order(request: HttpRequest):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders_list')
    else:
        form = OrderForm()
    return render(request, 'shopapp/order_create.html', {'form': form})
