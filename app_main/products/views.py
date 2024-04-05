from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from products.models import Products, Categories
from products.utils import query_search


def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        products = Products.objects.all()
    elif query:
        products = query_search(query)
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        products = Products.objects.filter(category=category)

    if on_sale:
        products = products.filter(discount__gt=0)

    if order_by and order_by != "default":
        products = products.order_by(order_by)


    paginator = Paginator(object_list=products, per_page=3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Catalog",
        "all_prod": current_page,
        "slug_url": category_slug
    }
    return render(request=request, template_name="products/catalog.html", context=context)



def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        "title": "Catalog",
        "product": product
    }
    return render(request=request, template_name="products/product.html", context=context)
