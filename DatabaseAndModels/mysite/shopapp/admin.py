from django.contrib import admin
from .models import Order, Product

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')  # Добавили поля, которые есть в модели Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')  # Добавили поля, которые есть в модели Product

admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
