from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list
    }
    return render(request, 'catalog/index.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        print(f'Данные пользователя: {name}, {number}')
    return render(request, 'catalog/contacts.html')


