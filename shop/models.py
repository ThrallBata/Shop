from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Товар')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    price = models.IntegerField()
    specification = models.CharField(max_length=500)
    warranty = models.CharField(max_length=4, verbose_name="Гарантия")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    # class Meta:
    #     verbose_name = 'Машины в наличии'
    #     verbose_name_plural = 'Машины в наличии'
    #     ordering = ['name_car']


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почтовый адрес')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    # class Meta:
    #     verbose_name = 'Клиенты'
    #     verbose_name_plural = 'Клиенты'
    #     ordering = ['car']


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    time = models.DateField()
    total_price = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Машина')
