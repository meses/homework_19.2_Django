from django.db import models
from slugify import slugify
from users.models import User

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


def gen_slug(string):
    finally_slug = slugify(string)
    return finally_slug

class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='Назавание')
    description = models.CharField(max_length=256, verbose_name='Описание')
    image = models.ImageField(upload_to='product_image/', verbose_name='Изображение', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, **NULLABLE)

    def __str__(self):
        return f'{self.title}, {self.price}, {self.category}'

    def get_image(self):
        return f'media/{self.image}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('title',)

    def get_active_version(self):
        """Получение активной версии"""
        return Versions.get_active_version(self) #Обращаемся к модели Versions, к функции получения версии

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')
    #created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Blog(models.Model):
    title = models.CharField(max_length=256, verbose_name='Назавание')
    slug = models.CharField(max_length=256, unique=True, verbose_name='URL')
    content = models.TextField(max_length=10000, verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog_preview/', verbose_name='Превью', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False ,verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}, {self.created_at}, Опубликовано:{self.is_published}'


    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('id',)


class Versions(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(verbose_name='Номер')
    title = models.CharField(max_length=100, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Активная')

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"

    def __str__(self):
        return self.title

    @classmethod
    def get_active_version(cls, product):
        """Получение активной версии по продукту"""
        try:
            return cls.objects.get(product=product, is_active=True)
        except:
            return None

