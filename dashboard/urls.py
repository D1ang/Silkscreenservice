from django.urls import path
from .views import dashboard, orderdetails

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('orderdetails/<str:pk_order>/', orderdetails, name='orderdetails'),
]
