from products.models import Products
from django.db.models import Q


def query_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    words_for_search = [word for word in query.split() if len(word) >= 3]

    q_object = Q()

    for word in words_for_search:
        q_object |= Q(description__icontains=word)
        q_object |= Q(name__icontains=word)
        print(word)

    return Products.objects.filter(q_object)