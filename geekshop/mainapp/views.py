from django.shortcuts import get_object_or_404, render
from .models import ProductCategory, Product

MENU_LINKS = [
    {
        'view_name': 'index', 
        'name': 'домой'
    },
    {
        'view_name': 'products:index',
        'name': 'продукты'
    },
    {
        'view_name': 'contact', 
        'name': 'контакты'
    }
]

def index(request):
 
    related_products = Product.objects.all()[:3]
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

def products(request, pk=None):
    if not pk:
        selected_category = ProductCategory.objects.first()
    else:
        selected_category = get_object_or_404(ProductCategory, id=pk)
    
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category=selected_category)
    return render(request, 'mainapp/products.html', 
    context={'title': 'продукты', 
            'menu_links': MENU_LINKS,
            'categories': categories,
            'selected_category': selected_category,
            'products': products})