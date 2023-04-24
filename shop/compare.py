from decimal import Decimal
import copy

from django.conf import settings
from .models import Product, Spec_gadget


class Compare(object):

    def __init__(self, request):
        """
        Инициализируем
        """
        self.session = request.session
        compare = self.session.get(settings.COMPARE_SESSION_ID)
        if not compare:
            # save an empty compare in the session
            compare = self.session[settings.COMPARE_SESSION_ID] = {}
        self.compare = compare

    def __iter__(self):
        """
        Перебор элементов  и получение продуктов из базы данных.
        """
        product_slug = self.compare.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_slug)
        compare = copy.deepcopy(self.compare)
        for product in products:
            compare[str(product.id)]['product'] = product

        for item in compare.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров.
        """
        return sum(item['quantity'] for item in self.compare.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        if product_id not in self.compare:
            self.compare[product_id] = {'quantity': 0,
                                        'price': str(product.price)}
        self.compare[product_id]['quantity'] = quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.COMPARE_SESSION_ID] = self.compare
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.compare:
            del self.compare[product_id]
            self.save()

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.compare.values())

    def clear(self):
        # удаление из сессии
        del self.session[settings.COMPARE_SESSION_ID]
        self.session.modified = True
