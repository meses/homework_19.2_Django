from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, category, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
        path('', ProductListView.as_view(), name='index'),
        path('contacts/', contacts, name='contacts'),
        path('category/', category, name='category'),
        path('product_add/', ProductCreateView.as_view(), name='product_add'),
        path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
        path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
        path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]