from django.core.management.base import BaseCommand
from shopapp.models import Product

class Command(BaseCommand):
    help = 'Создает продукты в базе данных'

    def handle(self, *args, **kwargs):
        products = [
            {'name': 'Product 1', 'description': 'Description 1', 'price': 100.00, 'stock': 10},
            {'name': 'Product 2', 'description': 'Description 2', 'price': 200.00, 'stock': 15},
            {'name': 'Product 3', 'description': 'Description 3', 'price': 150.00, 'stock': 5},
        ]
        for product in products:
            Product.objects.get_or_create(
                name=product['name'],
                description=product['description'],
                price=product['price'],
                stock=product['stock']
            )
        self.stdout.write(self.style.SUCCESS('Продукты успешно созданы!'))
