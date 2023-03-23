from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
# from .forms import SearchForm
# from haystack.query import SearchQuerySet

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

    return render(request,
                  'shop/index.html',
                  context=context)


def about(request):
    return render(request,
                  'shop/about.html',
                  {'menu': menu,
                   'title': 'О сайте'})


# def post_search(request):
#     form = SearchForm()
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             cd = form.cleaned_data
#             results = SearchQuerySet().models(Product).filter(content=cd['query']).load_all()
#             # count total results
#             total_results = results.count()
#     return render(request,
#                   'shop/search.html',
#                   {'form': form,
#                    'cd': cd,
#                    'results': results,
#                    'total_results': total_results})


def addpage(request):
    return HttpResponse("Обратная связь")


def contact(request):
    return render(request,
                  'shop/contact.html',
                  {'menu': menu,
                   'title': "Обратная связь"})


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'menu': menu,
        'title': product.name,
        'cat_selected': product.category_id,
        'cart_product_form': cart_product_form,
    }

    return render(request,
                  'shop/product.html',
                  context=context)


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

    return render(request,
                  'shop/index.html',
                  context=context)
