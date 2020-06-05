from django.urls import path
from .views import item_list, ItemDetailView, add_to_cart

app_name = 'orders'

urlpatterns = [
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
]
