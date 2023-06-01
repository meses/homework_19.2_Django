from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}

class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='Назавание')
    description = models.CharField(max_length=256, verbose_name='Описание')
    image = models.ImageField(upload_to='product_image/', verbose_name='Изображение', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.price}, {self.category}'

    def get_image(self):
        return f'media/{self.image}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('title',)

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')
    #created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
