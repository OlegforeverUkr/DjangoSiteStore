from django.shortcuts import render

from products.models import Products


def catalog(request):
    products = Products.objects.all()

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
