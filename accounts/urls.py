from django.urls import path
from .views import (
    adminpage,
    customerpage,
    orderdetails,
    update_order,
    userprofile
)

app_name = 'accounts'

urlpatterns = [
    path('', customerpage, name='customerpage'),
    path('admin/', adminpage, name='adminpage'),

    path('orderdetails/<str:pk_order>/', orderdetails, name='orderdetails'),
    path('update_order/<str:pk_order>/', update_order, name='update_order'),
    path('userprofile/', userprofile, name='userprofile'),
]
