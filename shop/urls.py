from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from django.conf import settings

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('search/', post_search, name='search'),
    path('product/<slug:product_slug>/', show_product, name='product'),
    path('category/<int:category_id>/', show_category, name='category'),
]


