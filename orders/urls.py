from django.urls import path
from .views import ItemListView, ItemDetailView, add_to_cart, remove_from_cart

app_name = 'orders'

urlpatterns = [
    path('products/', ItemListView.as_view(), name='products'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart')
]
