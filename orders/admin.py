from django.contrib import admin
from .models import Item, ItemTag, OrderItem, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'clicks'
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemTag)
admin.site.register(OrderItem)
admin.site.register(Order)
