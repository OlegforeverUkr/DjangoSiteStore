from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from baskets.models import Basket
from baskets.utils import get_user_baskets
from products.models import Products
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def basket_add(request):
    try:
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        if request.user.is_authenticated:
            carts = Basket.objects.filter(user=request.user, product=product)
            if carts.exists():
                carts = carts.first()
                if carts:
                    carts.quantity += 1
                    carts.save()
            else:
                Basket.objects.create(user=request.user, product=product, quantity=1)

        else:
            carts = Basket.objects.filter(session_key=request.session.session_key, product=product)

            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Basket.objects.create(session_key=request.session.session_key, product=product, quantity=1)


        user_cart = get_user_baskets(request)
        cart_items_html = render_to_string(
            "baskets/includes/included_basket.html", {"carts": user_cart}, request=request)

        response_data = {
            "message": "Товар добавлен в корзину",
            "cart_items_html": cart_items_html,
        }

        return JsonResponse(response_data)

    except ObjectDoesNotExist:
        messages.warning(request=request, message=f"{request.user.username}, товар не найден!!!")
        return redirect(request.META["HTTP_REFERER"])




def basket_change(request):
    try:
        cart_id = request.POST.get("cart_id")
        quantity = request.POST.get("quantity")

        cart = Basket.objects.get(id=cart_id)

        cart.quantity = quantity
        cart.save()
        updated_quantity = cart.quantity

        cart = get_user_baskets(request)
        cart_items_html = render_to_string(
            "baskets/includes/included_basket.html", {"carts": cart}, request=request)

        response_data = {
            "message": "Количество изменено",
            "cart_items_html": cart_items_html,
            "quaantity": updated_quantity,
        }

        return JsonResponse(response_data)
    
    except ObjectDoesNotExist:
        messages.warning(request=request, message=f"{request.user.username}, товар не найден!!!")
        return redirect(request.META["HTTP_REFERER"])




def basket_remove(request):
    try:
        cart_id = request.POST.get("cart_id")
        cart = Basket.objects.get(id=cart_id)
        quanity = cart.quantity
        cart.delete()

        user_cart = get_user_baskets(request)
        cart_items_html = render_to_string(
        "baskets/includes/included_basket.html", {"carts": user_cart}, request=request)

        response_data = {
            "message": "Товар удален из корзины",
            "cart_items_html": cart_items_html,
            "quantity_deleted": quanity
        }

        return JsonResponse(response_data)
    
    except ObjectDoesNotExist:
        messages.warning(request=request, message=f"{request.user.username}, товар не найден!!!")
        return redirect(request.META["HTTP_REFERER"])
