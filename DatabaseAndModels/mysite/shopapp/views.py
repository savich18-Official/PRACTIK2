from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Главная страница магазина</h1><ul><li><a href='/products/'>Список продуктов</a></li><li><a href='/orders/'>Список заказов</a></li></ul>")
