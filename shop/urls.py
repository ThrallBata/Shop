from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from django.conf import settings

from .views import *


urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('search/', post_search, name='search'),
    path('product/<slug:product_slug>/', show_product, name='product'),
    path('category/<slug:cat_slug>/', ShopCategory.as_view(), name='category'),
]


