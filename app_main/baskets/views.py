from django.shortcuts import redirect
from baskets.models import Basket
from products.models import Products


def basket_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Basket.objects.filter(user=request.user, product=product)
        if carts.exists():
            carts = carts.first()
            if carts:
                carts.quantity += 1
                carts.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)

        return redirect(request.META["HTTP_REFERER"])




def basket_change(request, product_slug):
    ...




def basket_remove(request, product_slug):
    ...
