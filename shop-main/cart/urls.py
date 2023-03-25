from django.urls import path
from .views import *

# app_name = 'cart'

urlpatterns = [
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<slug:product_slug>/', cart_add, name='cart_add'),
    path('cart/remove/<slug:product_slug>/', cart_remove, name='cart_remove'),
]