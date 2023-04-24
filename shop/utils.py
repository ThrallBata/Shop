from django.db.models import Count

from .models import *
from cart.forms import CartAddProductForm
from .forms import SearchForm, RegisterUserForm, LoginUserForm


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Сравнение", 'url_name': 'compare_detail'},
        {'title': "Корзина", 'url_name': 'cart_detail'}]


class DataMixin:
    # paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.annotate(Count('product'))

        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)

        context['menu'] = user_menu

        context['form_search'] = SearchForm()

        # context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
