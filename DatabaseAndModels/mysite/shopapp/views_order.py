from django.shortcuts import render
from shopapp.models import Order

def order_list(request):
    orders = Order.objects.all().prefetch_related('products', 'customer')
    return render(request, 'shopapp/order_list.html', {'orders': orders})
