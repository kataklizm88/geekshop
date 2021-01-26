from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'главная страница',
        'date' : 'Текущее время: ',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'каталог',
        'date': 'Текущее время: ',
        'categories': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'path': 'Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'path': 'Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'path': 'Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00',
             'description': 'Плотная ткань. Легкий материал.',
             'path': 'Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00',
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'path': 'Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'path': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        ]
    }
    return render(request, 'mainapp/products.html', context)
