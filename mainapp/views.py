from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    context = {
        'title': 'главная страница',
        'date' : 'Текущее время: ',
    }
    return render(request, 'mainapp/index.html', context)


# def products(request, category_id=None):
#     context = {'categories': ProductCategory.objects.all()}
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#         context.update({'products': products})
#     else:
#         context.update({'products': Product.objects.all()})
#
#     return render(request, 'mainapp/products.html', context)

def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products.order_by('price'), per_page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'categories': ProductCategory.objects.all(), 'products': products_paginator
    }
    return render(request, 'mainapp/products.html', context)

