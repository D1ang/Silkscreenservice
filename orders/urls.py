from django.urls import path
from .views import (
    ItemListView,
    OrderSummaryView,
    CheckoutView,
    PaymentView,
    add_to_cart,
    remove_from_cart
)

app_name = 'orders'

urlpatterns = [
    path('services/', ItemListView.as_view(), name='services'),
    path('cart/', OrderSummaryView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),

    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart')
]
