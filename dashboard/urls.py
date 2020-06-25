from django.urls import path
from .views import adminpage, customerpage, orderdetails, userprofile

app_name = 'dashboard'

urlpatterns = [
    path('', customerpage, name='customerpage'),
    path('admin/', adminpage, name='adminpage'),

    path('orderdetails/<str:pk_order>/', orderdetails, name='orderdetails'),
    path('userprofile/', userprofile, name='userprofile'),
]
