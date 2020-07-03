from django.contrib import admin
from .models import Payment, BillingAddress


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
    search_fields = (
        'user',
        'street_address',
        'city',
        'country'
    )


admin.site.register(Payment)
admin.site.register(BillingAddress, BillingAddressAdmin)
