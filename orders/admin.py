from django.contrib import admin
from .models import Item, ItemTag, OrderItem, Order

admin.site.register(Item)
admin.site.register(ItemTag)
admin.site.register(OrderItem)
admin.site.register(Order)
