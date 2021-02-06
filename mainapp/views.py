from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {
        'title': 'главная страница',
        'date' : 'Текущее время: ',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
