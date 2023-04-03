from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from cart.forms import CartAddProductForm
from .forms import SearchForm, LoginForm, RegisterUserForm

from .models import *
from .utils import *


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Корзина", 'url_name': 'cart_detail'}]


def index(request):
    products = Product.objects.all()
    form_search = SearchForm()
    context = {
        'products': products,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
        'form_search': form_search
    }

    return render(request,
                  'shop/index.html',
                  context=context)


def about(request):
    return render(request,
                  'shop/about.html',
                  {'menu': menu,
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
    return render(request,
                  'shop/contact.html',
                  {'menu': menu,
                   'title': "Обратная связь"})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})


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


def show_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    form_search = SearchForm()
    if len(products) == 0:
        raise Http404()

    context = {
        'products': products,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': category_id,
        'form_search': form_search,
    }

    return render(request,
                  'shop/index.html',
                  context=context)
