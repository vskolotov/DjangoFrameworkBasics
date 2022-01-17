from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from cartapp.models import Cart
from mainapp.models import Product

# Create your views here.
@login_required
def cart(request):
    title = 'корзина'  
    cart_items = Cart.objects.filter(user=request.user).\
                                  order_by('product__category')
    
    content = {
        'title': title,
        'cart_items': cart_items,
    }

    return render(request, 'cartapp/cart.html', content)

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    cart = Cart.objects.filter(user=request.user, product=product).first()

    if not cart:
        cart = Cart(user=request.user, product=product)

    cart.quantity += 1
    cart.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def remove_from_cart(request, pk):
    cart_record = get_object_or_404(Cart, pk=pk)
    cart_record.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
