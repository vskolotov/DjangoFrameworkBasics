from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from cartapp.models import Cart
from mainapp.models import Product
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.
@login_required
def cart(request):
    title = 'корзина'
    cart_items = Cart.objects.filter(user=request.user).order_by('product__category')

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


@login_required
def cart_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_cart_item = Cart.objects.get(pk=int(pk))

        if quantity > 0:
            new_cart_item.quantity = quantity
            new_cart_item.save()
        else:
            new_cart_item.delete()

        cart_items = Cart.objects.filter(user=request.user).order_by('product__category')

        content = {
            'cart_items': cart_items,
        }

        result = render_to_string('cartapp/includes/inc_cart_list.html', content)

        return JsonResponse({'result': result})
