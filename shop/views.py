from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView

from cart.forms import CartAddProductForm
from wishlist.forms import WishlistAddProductForm
from .compare import Compare
from .forms import CompareAddProductForm
from .models import *
from .utils import *


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Корзина", 'url_name': 'cart_detail'}]


class ShopHome(DataMixin, ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        v_def = self.get_user_context(cart_product_form=CartAddProductForm)
        b_def = self.get_user_context(wishlist_product_form=WishlistAddProductForm)
        return dict(list(context.items()) + list(c_def.items()) + list(v_def.items()) + list(b_def.items()))

# def index(request):
#     products = Product.objects.all()
#     form_search = SearchForm()
#     context = {
#         'products': products,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#         'form_search': form_search
#     }
#
#     return render(request,
#                   'shop/index.html',
#                   context=context)


def about(request):
    form_search = SearchForm()
    return render(request, 'shop/about.html',
                  {'menu': menu,
                   'form_search': form_search,
                   'title': 'О сайте'})


def post_search(request):
    if request.method == 'GET':
        form_search = SearchForm(request.GET)

        if form_search.is_valid():
            query = form_search.cleaned_data.get("query")
            products = Product.objects.filter(name__icontains=query)
            return render(request, 'shop/index.html', {'menu': menu,  'products': products,
                                                       'form_search': form_search})


def contact(request):
    form_search = SearchForm()
    return render(request,
                  'shop/contact.html',
                  {'menu': menu,
                   'form_search': form_search,
                   'title': "Обратная связь"})


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart_product_form = CartAddProductForm()
    form_search = SearchForm()
    context = {
        'product': product,
        'menu': menu,
        'title': product.name,
        'cat_selected': product.category_id,
        'cart_product_form': cart_product_form,
        'form_search': form_search,
    }
    return render(request,
                  'shop/product.html',
                  context=context)


class ShopCategory(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['form_search'] = SearchForm()
        context['cat_selected'] = context['products'][0].category.id
        return context


def profile(request):
    form_search = SearchForm()
    context = {
        'menu': menu,
        'form_search': form_search,
    }
    if request.user.is_authenticated:
        return render(request,
                      'shop/profile.html',
                      context=context)
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')


@require_POST
def compare_add(request, product_slug):
    compare = Compare(request)
    product = get_object_or_404(Product, slug=product_slug)
    form = CompareAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        compare.add(product=product,
                     update_quantity=cd['update'])
    return redirect('compare_detail')


def compare_remove(request, product_slug):
    compare = Compare(request)
    product = get_object_or_404(Product, slug=product_slug)
    compare.remove(product)
    return redirect('compare_detail')


def compare_detail(request):
    compare = Compare(request)
    context = {'compare': compare,
               'menu': menu}
    return render(request, 'shop/compare.html', context)
