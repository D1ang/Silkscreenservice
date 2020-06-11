from django.contrib import admin
from .models import Item, ItemTag, OrderItem, Order, Payment


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
        'id_code',
        'date',
        'status',
        'ordered',
        'billing_address',
        'payment'
    )
    list_display_links = (
        'id_code',
        'billing_address',
        'payment'
    )
    list_filter = (
        'ordered',
    )
    search_fields = (
        'user__username',
        'id_code'
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemTag, ItemTagAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
