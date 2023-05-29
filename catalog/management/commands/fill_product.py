from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_lst = [
            {'title': '������� Huawei MateBook D 15 BOD-WDI9', 'description': '15.6", IPS, Intel Core i3 1115G4 3���, 2-�������, 8�� DDR4, 256�� SSD, Intel UHD Graphics , ��� ������������ �������, ����� ������ [53013sdv]', 'price': 42999, 'category': Category.objects.get(title='��������')},
            {'title': '������� HIPER Workbook N15RP, 15.6', 'description': 'AMD Ryzen 5 3500U 2.1���, 4-�������, 16�� DDR4, 512�� SSD, AMD Radeon Vega 8, Windows 10 Professional, ������ [n15rp96wi]', 'price': 44990, 'category': Category.objects.get(title='��������')},
            {'title': '������� ������� HIPER G16', 'description': '16.1", Intel Core i5 10400 2.9���, 6-�������, 16�� DDR4, 512�� SSD, NVIDIA GeForce RTX 3070 ��� ��������� - 8 ��, ��� ������������ �������, ������ [g16rtx3070a10400lx]', 'price': 125990, 'category': Category.objects.get(title='��������')},
            {'title': '�������� Huawei Mate 50 Pro 8/512Gb', 'description': '���������', 'price': 79990, 'category': Category.objects.get(title='���������')},
            {'title': '�������� REALME C25s 4/64Gb', 'description': '�����', 'price': 8990, 'category': Category.objects.get(title='���������')},
            {'title': '50" ��������� HAIER Smart TV S1', 'description': '4K Ultra HD, ������, ����� ��, Android', 'price': 27990, 'category': Category.objects.get(title='����������')},
            {'title': '43" ��������� Xiaomi Mi TV A2', 'description': '4K Ultra HD, ������, ����� ��, Android', 'price': 24990, 'category': Category.objects.get(title='����������')},
            {'title': '������� Huawei MateView SE SSN-24 23.8"', 'description': '������ [53060683]', 'price': 11990, 'category': Category.objects.get(title='��������')},
        ]

        products_for_append = []

        for product in products_lst:
            products_for_append.append(Product(**product))

        products_for_delete = Product.objects.all()
        if len(products_for_delete) > 0:
            for product in products_for_delete:
                product.delete()

        Product.objects.bulk_create(products_for_append)