from django.contrib import admin
from .models import Order, Product

# Inline для отображения заказов на странице продукта
class OrderInline(admin.TabularInline):
    model = Order.products.through
    extra = 0  # без пустых строк

# Действие для архивирования продуктов
@admin.action(description="Архивировать выбранные продукты")
def mark_as_archived(modeladmin, request, queryset):
    queryset.update(is_archived=True)

# Админка для заказов
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    search_fields = ('customer__username', 'id')

# Админка для продуктов
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name', 'price')  # строковое и числовое поле
    inlines = [OrderInline]  # отображение заказов на странице продукта

    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Цены', {
            'fields': ('price', 'discount')
        }),
        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('is_archived',),
        }),
    )

    actions = [mark_as_archived]  # групповое действие

# Регистрация моделей в админке
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
