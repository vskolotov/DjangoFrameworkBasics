from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from cartapp.models import Cart
from mainapp.models import Product

# Create your views here.
def cart(request):
    content = {
        'cart': request.user.cart.all(),
    }

    return render(request, 'cartapp/cart.html', content)

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    cart = Cart.objects.filter(user=request.user, product=product).first()

    if not cart:
        cart = Cart(user=request.user, product=product)

    cart.quantity += 1
    cart.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_from_cart(request, pk):
    content = {}
    return render(request, 'cartapp/cart.html', content)