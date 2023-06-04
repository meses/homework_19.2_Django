from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Category, Product
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

#def product(request, pk):
#    product_item = Product.objects.get(pk=pk)
#    context = {
#        'product' : product_item,
#        'title': 'Товар',
#        'company_title': company_name
#    }
#    return render(request, 'catalog/product_detail.html', context)

#def index(request):
#    product_list = Product.objects.all()
#    context = {
#        'product_list': product_list,
#        'title': 'Товары',
#        'company_title': company_name
#    }
#    return render(request, 'catalog/product_list.html', context)


#def product_add(request):
#    category_list = Category.objects.all()
#    content = {
#        'category_list': category_list
#    }
#    if request.method == 'POST':
#        title = request.POST.get('title')
#        description = request.POST.get('description')
#        price = request.POST.get('price')
#        category_id = request.POST.get('category_id')
#        Product.objects.create(title=title, description=description, price=price, category_id=category_id)
#        #print(f'{title}, {category_id}')
#
#    return render(request, 'catalog/product_add.html', content)

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


