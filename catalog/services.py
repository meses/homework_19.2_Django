from django.conf import settings
from django.core.mail import send_mail

from catalog.models import Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def send_congratuation_email():
    send_mail(
        'Поздравляем!',
        'Статья набрала сто просмотров',
        settings.EMAIL_HOST_USER,
        recipient_list=['dvayuzer@yandex.ru']
    )

def get_categories():
    '''Сервисная функция, которая будет отвечать за выборку категорий + низкоуровневое кэширование'''
    if CACHE_ENABLED:
        key = f'categories_list'
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(categories_list, categories_list)
    else:
        categories_list = Category.objects.all()

    return categories_list