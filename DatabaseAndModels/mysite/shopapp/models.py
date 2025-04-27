from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Для работы с временем

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает обработки'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, сделавший заказ
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)  # Статус заказа
    products = models.ManyToManyField(Product)  # Продукты в заказе
    created_at = models.DateTimeField(default=timezone.now)  # Время создания заказа

    def __str__(self):
        return f"Заказ #{self.id} от {self.customer.username}"
