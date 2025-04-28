from django.shortcuts import render
from shopapp.models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shopapp/product_list.html', {'products': products})
