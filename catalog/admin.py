from django.contrib import admin

from catalog.models import Product, Category, Blog

# Register your models here.
#admin.site.register(Product)
#admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'is_published', 'views_count',)
    list_filter = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}
