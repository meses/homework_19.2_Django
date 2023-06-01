from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, category, product_add

app_name = CatalogConfig.name

urlpatterns = [
        path('', index, name='index'),
        path('contacts/', contacts, name='contacts'),
        path('category/', category, name='category'),
        path('product_add/', product_add, name='product_add')
]