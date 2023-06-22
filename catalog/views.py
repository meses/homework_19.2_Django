from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, VersionsForm
from catalog.models import Category, Product, Blog, Versions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.services import send_congratuation_email


# Create your views here.
company_name = 'Магазин на диване'

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Товары',
        'company_title': company_name
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['object_list']
        for product in products:
            product.get_active_version()
        return context

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object().title
        return context_data

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    #fields = ('title', 'description', 'price', 'category',)
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Создать товар',
        'company_title': company_name
    }

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Изменить товар',
        'company_title': company_name
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionsFormset = inlineformset_factory(Product, Versions, form=VersionsForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionsFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionsFormset(instance=self.object)
        return context_data
    
    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)

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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogListViewNotPublished(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог магазина',
        'company_title': company_name
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=False)
        return queryset

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
    extra_context = {
        'title': 'Изменить пост',
        'company_title': company_name
    }

    def get_success_url(self):
        return reverse_lazy('catalog:post_detail', kwargs={'pk': self.kwargs['pk']})

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
        self.object.views_count += 1
        self.object.save()
        return context_data

    def get_object(self, queryset=None):
        object = Blog.objects.get(pk=self.kwargs['pk'])
        if object.views_count == 100:
            send_congratuation_email()
            pass
        return object

def toggle_published(request, pk):
    post_item = get_object_or_404(Blog, pk=pk)
    if post_item.is_published:
        post_item.is_published = False
    else:
        post_item.is_published = True

    post_item.save()

    return redirect(reverse('catalog:post_update', args=[post_item.pk]))

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории',
        'company_title': company_name
    }

class CategoryCreateView(CreateView):
    model = Category
    fields = ('title', 'description',)
    success_url = reverse_lazy('catalog:category')
    extra_context = {
        'title': 'Создать категорию',
        'company_title': company_name
    }

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('title', 'description',)
    success_url = reverse_lazy('catalog:category')
    extra_context = {
        'title': 'Изменить категорию',
        'company_title': company_name
    }

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:category')
    extra_context = {
        'title': 'Удалить категорию',
        'company_title': company_name
    }

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        print(f'Данные пользователя: {name}, {number}')
    return render(request, 'catalog/contacts.html')


