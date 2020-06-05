from django.contrib import admin
from .models import Item, ItemTag, OrderItem, Order


class ItemTagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'colour'
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'tag',
        'price',
        'clicks'
    )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'user',
        'quantity',
        'ordered'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'user',
        'status',
        'ordered'
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemTag, ItemTagAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
