from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'title': 'Ноутбуки', 'description': 'Категория Ноутбуки'},
            {"title": "Смартфоны", "description": "Категория Смартфоны"},
            {"title": "Телевизоры", "description": "Категория Телевизоры"}
        ]

        category_for_append = []

        for item in category_list:
            category_for_append.append(Category(**item))

        lst = Category.objects.all()
        if len(lst) > 0:
            for item in lst:
                item.delete()
        Category.objects.bulk_create(category_for_append)
