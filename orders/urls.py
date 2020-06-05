from django.urls import path
from .views import ItemListView, ItemDetailView, add_to_cart

app_name = 'orders'

urlpatterns = [
    path('products/', ItemListView.as_view(), name='products'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
]
