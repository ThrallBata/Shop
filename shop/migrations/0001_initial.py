# Generated by Django 4.1.7 on 2023-03-23 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почтовый адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Spec_gadget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_product', models.CharField(max_length=50)),
                ('cpu', models.CharField(max_length=50, verbose_name='Процессор')),
                ('frequency', models.FloatField()),
                ('memory', models.IntegerField()),
                ('size', models.CharField(max_length=50)),
                ('warranty', models.CharField(max_length=15, verbose_name='Гарантия')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Товар')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('specification', models.CharField(max_length=2000)),
                ('warranty', models.CharField(max_length=15, verbose_name='Гарантия')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.category')),
                ('spec_gadget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.spec_gadget')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('total_price', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.client', verbose_name='Машина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар')),
            ],
        ),
    ]
