from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import *


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def index(request):
    products = Product.objects.all()
    cats = Category.objects.all()

    context = {
        'products': products,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'shop/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_product(request, prod_id):
    return HttpResponse(f"Отображение статьи с id = {prod_id}")


def show_category(request, cat_id):
    products = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(products) == 0:
        raise Http404()

    context = {
        'products': products,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'shop/index.html', context=context)