from django.urls import path
from .views import address, payment

urlpatterns = [
    path('address/', address, name='address_list'),
    path('payment/', payment, name='payment'),
]