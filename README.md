# Сайт для аренды автомобилей 

## Для запуска сервиса необходимо :
0. Склонировать репозиторий
1. Установить зависимости `pip install -r requirements.txt`
2. Необходимо установить свои данные в файле **.env** для подключения к БД и сделать миграции `python manage.py migrate`.
3. Необходимо создать администратора `python manage.py createsuperuser`.
4. Запустить сервер `python manage.py runserver` , обязательно находиться в корневой папке.
5. Для заполнения сайта товарами необходимо зайти в админку по адресу ***localhost/admin***.

## Функционал:
На сайте все необходимые функции онлайн магазина такие как:
0. Корзина и избранное по сессии пользователя.
1. Оформление заказа.
2. Регистрация и авторизация.
3. Сравнение товаров.
4. Поиск по названию товаров.
5. Отображение карточек товаров и разделение их по категориям.