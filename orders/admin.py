from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Item, ItemTag, OrderItem, Order, Payment, BillingAddress


def set_status_pending(modeladmin, request, queryset):
    queryset.update(status='pending')


def set_status_finished(modeladmin, request, queryset):
    queryset.update(status='finished')


set_status_pending.short_description = 'Set status to pending'
set_status_finished.short_description = 'Set status to finished'


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
        'billing_address',
        'payment',
        'ordered',
        'status'
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
    actions = (
        set_status_pending,
        set_status_finished
    )


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'street_address',
        'address_line_2',
        'city',
        'region',
        'postal',
        'country'
    )
    list_filter = (
        'country',
    )
    search_fields = (
        'user',
        'street_address',
        'city',
        'country'
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemTag, ItemTagAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(BillingAddress, BillingAddressAdmin)

admin.site.unregister(Group)
