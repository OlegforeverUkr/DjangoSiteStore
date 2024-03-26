from django.shortcuts import get_list_or_404, render

from products.models import Products


def catalog(request, category_slug):

    if category_slug == "all":
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        "title": "Catalog",
        "all_prod": products
    }
    return render(request=request, template_name="products/catalog.html", context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        "title": "Catalog",
        "product": product
    }
    return render(request=request, template_name="products/product.html", context=context)
