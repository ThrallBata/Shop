from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404

from .models import *


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'shop/index.html', context=context)


def about(request):
    return render(request, 'shop/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product,
        'menu': menu,
        'title': product.name,
        'cat_selected': product.category_id,
    }

    return render(request, 'shop/product.html', context=context)


def show_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)

    if len(products) == 0:
        raise Http404()

    context = {
        'products': products,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': category_id,
    }

    return render(request, 'shop/index.html', context=context)