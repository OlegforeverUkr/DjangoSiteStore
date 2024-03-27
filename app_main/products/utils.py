from products.models import Products
from django.db.models import Q


def query_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))