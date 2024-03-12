from django.contrib import admin
from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    search_fields = ['address']
    search_help_text = 'Поиск по адресу'
    fieldsets = [
        (
            "Основная информация", {
                'fields': ['name', 'email', 'phone_number']
            }
        ),
        (
            "Ещё", {
                'classes': ['collapse'],
                'fields': ['address', 'date_registration'],
                'description': "Дополнительная информация о клиенте"
            }
        )
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'price', 'quantity']
    ordering = ['quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'product', 'product_price', 'total_amount', 'client']
    ordering = ['client', '-order_date']