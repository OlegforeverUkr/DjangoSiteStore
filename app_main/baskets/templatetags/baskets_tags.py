from django import template
from baskets.models import Basket


register = template.Library()


@register.simple_tag()
def user_carts(request):
    return Basket.objects.filter(user=request.user)