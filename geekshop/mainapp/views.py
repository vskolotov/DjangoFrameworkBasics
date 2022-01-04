import random
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from cartapp.models import Cart
from .models import ProductCategory, Product

MENU_LINKS = [
    {
        'view_name': 'index',
        'namespace': '',
        'full_href': 'index', 
        'name': 'домой'
    },
    {
        'view_name': 'index',
        'namespace': 'products',
        'full_href': 'products:index',
        'name': 'продукты'
    },
    {
        'view_name': 'contact', 
        'namespace': '',
        'full_href': 'contact',
        'name': 'контакты'
    }
]

def index(request):

    related_products = Product.objects.all()[:3]
    return render(request, 'mainapp/index.html', 
    context={'title': 'главная', 
            'menu_links': MENU_LINKS,
            'related_products': related_products,
            })           

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
            'contacts': contacts,
            })

def get_hot_product():
    products = Product.objects.all()
    return random.choice(list(products))

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products

def products(request, pk=None):

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    cart = []
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    if not pk:
        selected_category = None
        selected_category_dict = {'name':'Всё', 'href': reverse('products:index')}
    else:
        selected_category = get_object_or_404(ProductCategory, id=pk)
        selected_category_dict = {'name': selected_category.name, 'href': reverse('products:category', args=[selected_category.id])}
    
    categories = [{'name': c.name, 'href': reverse('products:category', args=[c.id])} for c in ProductCategory.objects.all()]
    categories = [{'name':'Всё', 'href': reverse('products:index')}, *categories]
    if selected_category:
        products = Product.objects.filter(category=selected_category)
        return render(request, 'mainapp/products_list.html', 
        context={'title': 'продукты', 
                'menu_links': MENU_LINKS,
                'categories': categories,
                'selected_category': selected_category_dict,
                'hot_prduct': hot_product, 
                'same_products': same_products,
                'products': products,
                'cart': cart})
    else:
        products = Product.objects.all()
    return render(request, 'mainapp/products.html', 
    context={'title': 'продукты', 
            'menu_links': MENU_LINKS,
            'categories': categories,
            'selected_category': selected_category_dict,
            'hot_prduct': hot_product,
            'same_products': same_products,
            'products': products,
            'cart': cart})

def product(request, pk):
    categories = [{'name': c.name, 'href': reverse('products:category', args=[c.id])} for c in ProductCategory.objects.all()]
    categories = [{'name':'Всё', 'href': reverse('products:index')}, *categories]
    content = {
        'title': 'продукты', 
        'product': get_object_or_404(Product, pk=pk),
        'menu_links': MENU_LINKS,
        'categories': categories,
    }
	
    return render(request, 'mainapp/product.html', content)