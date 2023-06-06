from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from catalog.models import Category, Product, Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
company_name = 'Магазин на диване'

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Товары',
        'company_title': company_name
    }

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object().title
        return context_data

class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'description', 'price', 'category',)
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Создать товар',
        'company_title': company_name
    }

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('title', 'description', 'price', 'category',)
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Изменить товар',
        'company_title': company_name
    }

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Удалить товар',
        'company_title': company_name
    }


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог магазина',
        'company_title': company_name
    }

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content',)
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'Создать пост',
        'company_title': company_name
    }

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content',)
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'Изменить пост',
        'company_title': company_name
    }

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'Удалить пост',
        'company_title': company_name
    }

class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object().title
        return context_data

def toggle_published(request, pk):
    post_item = get_object_or_404(Blog, pk=pk)
    if post_item.is_published:
        post_item.is_published = False
    else:
        post_item.is_published = True

    post_item.save()

    return redirect(reverse('catalog:post_update', args=[post_item.pk]))

def category(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
        'title': 'Категории',
        'company_title': company_name
    }
    return render(request, 'catalog/category.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        print(f'Данные пользователя: {name}, {number}')
    return render(request, 'catalog/contacts.html')


