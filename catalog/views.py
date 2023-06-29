from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, VersionsForm
from catalog.models import Category, Product, Blog, Versions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.services import send_congratuation_email


# Create your views here.
company_name = 'Магазин на диване'

class ProductListView(LoginRequiredMixin, ListView):
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

class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object().title
        return context_data

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    #fields = ('title', 'description', 'price', 'category',)
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Создать товар',
        'company_title': company_name
    }

    def form_valid(self, form):
        form = ProductForm(data=self.request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user_id = self.request.user
            product.save()
        return HttpResponseRedirect(reverse('catalog:index'))

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
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


    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        print(object.user_id)
        print(self.request.user)
        if object.user_id != self.request.user:
            raise Http404("Вы не являетесь владельцем продукта.")
        return object


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Удалить товар',
        'company_title': company_name
    }


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    extra_context = {
        'title': 'Блог магазина',
        'company_title': company_name
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogListViewNotPublished(LoginRequiredMixin, ListView):
    model = Blog
    extra_context = {
        'title': 'Блог магазина',
        'company_title': company_name
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=False)
        return queryset

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content',)
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'Создать пост',
        'company_title': company_name
    }

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content',)
    extra_context = {
        'title': 'Изменить пост',
        'company_title': company_name
    }

    def get_success_url(self):
        return reverse_lazy('catalog:post_detail', kwargs={'pk': self.kwargs['pk']})

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'Удалить пост',
        'company_title': company_name
    }

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object().title
        self.object.views_count += 1
        self.object.save()
        return context_data

    def get_object(self, queryset=None):
        object = Blog.objects.get(pk=self.kwargs['pk'])
        if object.views_count == 1:
            send_congratuation_email()
        return object

@login_required
def toggle_published(request, pk):
    post_item = get_object_or_404(Blog, pk=pk)
    if post_item.is_published:
        post_item.is_published = False
    else:
        post_item.is_published = True

    post_item.save()

    return redirect(reverse('catalog:post_update', args=[post_item.pk]))

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    extra_context = {
        'title': 'Категории',
        'company_title': company_name
    }

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ('title', 'description',)
    success_url = reverse_lazy('catalog:category')
    extra_context = {
        'title': 'Создать категорию',
        'company_title': company_name
    }

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ('title', 'description',)
    success_url = reverse_lazy('catalog:category')
    extra_context = {
        'title': 'Изменить категорию',
        'company_title': company_name
    }

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
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


