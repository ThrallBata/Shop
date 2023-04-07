from django.urls import path
from .views import *

urlpatterns = [
    path('wishlist/', wishlist_detail, name='wishlist_detail'),
    path('wishlist/add/<slug:product_slug>/', wishlist_add, name='wishlist_add'),
    path('wishlist/remove/<slug:product_slug>/', wishlist_remove, name='wishlist_remove'),
]
