from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.
company_name = 'Магазин на диване'

def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'title': 'Товары',
        'company_title': company_name
    }
    return render(request, 'catalog/index.html', context)

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


