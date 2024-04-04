from django.shortcuts import redirect
from baskets.models import Basket
from products.models import Products
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


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

        messages.success(request=request, message=f"{request.user.username}, {product.name} добавлен в корзину.")

        return redirect(request.META["HTTP_REFERER"])




def basket_change(request, product_slug):
    ...




def basket_remove(request, basket_id):
    try:
        basket = Basket.objects.get(id=basket_id)
        basket.delete()
        messages.success(request=request, message=f"{request.user.username}, товар {basket.product.name} удален.")
        return redirect(request.META["HTTP_REFERER"])
    
    except ObjectDoesNotExist:
        messages.warning(request=request, message=f"{request.user.username}, товар не найден!!!")
        return redirect(request.META["HTTP_REFERER"])
