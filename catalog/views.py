from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        print(f'Данные пользователя: {name}, {number}')
    return render(request, 'catalog/contacts.html')


