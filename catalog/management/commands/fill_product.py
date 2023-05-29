from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_lst = [

        ]

        products_for_append = []

        for product in products_lst:
            products_for_append.append(Product(**product))

        products_for_delete = Product.objects.all()
        if len(products_for_delete) > 0:
            for product in products_for_delete:
                product.delete()

        Product.objects.bulk_create(products_for_append)