from django.core.management.base import BaseCommand
from shopapp.models import Order, Product
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Создает заказы для пользователей'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        products = Product.objects.all()
        for user in users:
            order = Order.objects.create(
                customer=user,
                status='Pending'
            )
            order.products.add(*products)
            order.save()
        self.stdout.write(self.style.SUCCESS('Заказы успешно созданы!'))
