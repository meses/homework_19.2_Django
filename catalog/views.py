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

def product_add(request):
    category_list = Category.objects.all()
    content = {
        'category_list': category_list
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category_id')
        Product.objects.create(title=title, description=description, price=price, category_id=category_id)
        #print(f'{title}, {category_id}')

    return render(request, 'catalog/product_add.html', content)

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


