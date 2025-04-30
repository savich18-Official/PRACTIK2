# myapp/forms.py

from django import forms
from .models import Product, Order  # Импортируем обе модели

# Форма для создания продукта
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

# Форма для создания заказа
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product', 'quantity']
