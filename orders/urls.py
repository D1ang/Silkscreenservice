from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart
)

app_name = 'orders'

urlpatterns = [
    path('services_list/', ItemListView.as_view(), name='services'),
    path('service/<slug>/', ItemDetailView.as_view(), name='service'),
    path('cart/', OrderSummaryView.as_view(), name='cart'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart')
]
