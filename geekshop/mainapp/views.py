from django.shortcuts import render

MENU_LINKS = [
    {
        'view_name': 'index', 
        'name': 'домой'
    },
    {
        'view_name': 'products',
        'name': 'продукты'
    },
    {
        'view_name': 'contact', 
        'name': 'контакты'
    }
]

def index(request):
    related_products = [
        {
            'name':'Светильник',
            'description':'Очень яркий',
            'img':'img/product-1.jpg'
        },
        {
            'name':'Стулья',
            'description':'Очень мягкие',
            'img':'img/product-2.jpg'
        },
        {
            'name':'Графин',
            'description':'Очень прочный',
            'img':'img/product-3.jpg'
        }
    ]
    
    return render(request, 'mainapp/index.html', 
    context={'title': 'главная', 
            'menu_links': MENU_LINKS,
            'related_products': related_products}
                )           

def contact(request):
    contacts = [
        {
            'city':'Москва',
            'telephone':'+7-888-888-8881',
            'email':'mos@geekshop.ru',
            'address':'В пределах МКАД'
        },
        {
            'city':'Ижевск',
            'telephone':'+7-888-888-8882',
            'email':'izh@geekshop.ru',
            'address':'ул. Центальная, 12'
        },
        {
            'city':'Урай',
            'telephone':'+7-888-888-8883',
            'email':'uray@geekshop.ru',
            'address':'ул. Ленина, 12'
        },
    ]
    return render(request, 'mainapp/contact.html', 
    context={'title': 'контакты', 
            'menu_links': MENU_LINKS,
            'contacts': contacts})

def products(request):
    product_menu = [
        {'href': 'products', 'name': 'все'},
        {'href': 'products#2', 'name': 'дом'},
        {'href': 'products#3', 'name': 'офис'},
        {'href': 'products#4', 'name': 'модерн'},
        {'href': 'products#5', 'name': 'класика'},
    ]

    related_products = [
        {
            'name':'Светильник',
            'description':'Очень яркий',
            'img':'img/product-11.jpg'
        },
        {
            'name':'Стул',
            'description':'Очень мягкий',
            'img':'img/product-21.jpg'
        },
        {
            'name':'Лампа',
            'description':'Очень экономичная',
            'img':'img/product-31.jpg'
        }
    ]
    return render(request, 'mainapp/products.html', 
    context={'title': 'продукты', 
            'menu_links': MENU_LINKS,
            'product_menu': product_menu,
            'related_products': related_products})