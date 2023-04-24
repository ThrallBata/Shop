from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .wishlist import Wishlist
from .forms import WishlistAddProductForm

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Корзина", 'url_name': 'cart_detail'}]


@require_POST
def wishlist_add(request, product_slug):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, slug=product_slug)
    form = WishlistAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        wishlist.add(product=product,
                     update_quantity=cd['update'])
    return redirect('wishlist_detail')


def wishlist_remove(request, product_slug):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, slug=product_slug)
    wishlist.remove(product)
    return redirect('wishlist_detail')


def wishlist_detail(request):
    wishlist = Wishlist(request)
    context = {'wishlist': wishlist,
               'menu': menu}
    return render(request, 'wishlist/detail.html', context)
