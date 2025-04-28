from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает обработки'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Заказ #{self.id} от {self.customer.username}"
