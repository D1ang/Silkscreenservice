from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
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


admin.site.register(Customer, CustomerAdmin)
