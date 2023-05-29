from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_lst = [
            {'title': 'Ноутбук Huawei MateBook D 15 BOD-WDI9', 'description': '15.6", IPS, Intel Core i3 1115G4 3ГГц, 2-ядерный, 8ГБ DDR4, 256ГБ SSD, Intel UHD Graphics , без операционной системы, серый космос [53013sdv]', 'price': 42999, 'category': Category.objects.get(title='Ноутбуки')},
            {'title': 'Ноутбук HIPER Workbook N15RP, 15.6', 'description': 'AMD Ryzen 5 3500U 2.1ГГц, 4-ядерный, 16ГБ DDR4, 512ГБ SSD, AMD Radeon Vega 8, Windows 10 Professional, черный [n15rp96wi]', 'price': 44990, 'category': Category.objects.get(title='Ноутбуки')},
            {'title': 'Ноутбук игровой HIPER G16', 'description': '16.1", Intel Core i5 10400 2.9ГГц, 6-ядерный, 16ГБ DDR4, 512ГБ SSD, NVIDIA GeForce RTX 3070 для ноутбуков - 8 ГБ, без операционной системы, черный [g16rtx3070a10400lx]', 'price': 125990, 'category': Category.objects.get(title='Ноутбуки')},
            {'title': 'Смартфон Huawei Mate 50 Pro 8/512Gb', 'description': 'оранжевый', 'price': 79990, 'category': Category.objects.get(title='Смартфоны')},
            {'title': 'Смартфон REALME C25s 4/64Gb', 'description': 'серый', 'price': 8990, 'category': Category.objects.get(title='Смартфоны')},
            {'title': '50" Телевизор HAIER Smart TV S1', 'description': '4K Ultra HD, черный, СМАРТ ТВ, Android', 'price': 27990, 'category': Category.objects.get(title='Телевизоры')},
            {'title': '43" Телевизор Xiaomi Mi TV A2', 'description': '4K Ultra HD, черный, СМАРТ ТВ, Android', 'price': 24990, 'category': Category.objects.get(title='Телевизоры')},
            {'title': 'Монитор Huawei MateView SE SSN-24 23.8"', 'description': 'черный [53060683]', 'price': 11990, 'category': Category.objects.get(title='Мониторы')},
        ]

        products_for_append = []

        for product in products_lst:
            products_for_append.append(Product(**product))

        products_for_delete = Product.objects.all()
        if len(products_for_delete) > 0:
            for product in products_for_delete:
                product.delete()

        Product.objects.bulk_create(products_for_append)