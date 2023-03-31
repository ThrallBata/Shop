from django import forms
from .models import Order
from django.forms import TextInput


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

        widgets = {
            'first_name': TextInput(attrs={
                "class": "order-input",
                "placeholder": "Ваше имя",
            }),
            'last_name': TextInput(attrs={
                "class": "order-input",
                "placeholder": "Ваша фамилия",
            }),
            'email': TextInput(attrs={
                "class": "order-input",
                "placeholder": "Email",
            }),
            'address': TextInput(attrs={
                "class": "order-input",
                "placeholder": "Адрес",
            }),
            'postal_code': TextInput(attrs={
                "class": "order-input",
                "placeholder": "Почтовый индекс",
            }),
            'city': TextInput(attrs={
                "class": "order-input",
                "placeholder": "Ваш город",
            })
        }
