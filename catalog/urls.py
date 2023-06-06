from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, category, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
        ProductDeleteView, BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, \
        toggle_published

app_name = CatalogConfig.name

urlpatterns = [
        path('', ProductListView.as_view(), name='index'),
        path('contacts/', contacts, name='contacts'),
        path('category/', category, name='category'),
        path('product_add/', ProductCreateView.as_view(), name='product_add'),
        path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
        path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
        path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
        path('blog/', BlogListView.as_view(), name='blog'),
        path('blog/create', BlogCreateView.as_view(), name='blog_add'),
        path('blog/post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
        path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='post_update'),
        path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete'),
        path('blog/toggle/<int:pk>', toggle_published, name='toggle_published')
]