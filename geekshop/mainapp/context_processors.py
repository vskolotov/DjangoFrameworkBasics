from cartapp.models import Cart


def card(request):
    card = []

    if request.user.is_authenticated:
        card = Cart.objects.filter(user=request.user)

    return {
        'card': card,
    }
