from django.contrib import admin
from .models import Payment, BillingAddress


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'first_name',
        'last_name',
        'street_address',
        'city',
        'region',
        'postal',
        'country'
    )
    search_fields = (
        'company_name',
        'street_address',
        'city',
        'country'
    )


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'amount'
    )


admin.site.register(Payment, PaymentAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
