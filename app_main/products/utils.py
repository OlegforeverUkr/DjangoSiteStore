from products.models import Products
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

def query_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    return Products.objects.annotate(rank=SearchRank(vector=vector, query=query)).filter(rank__gt=0).order_by("-rank")
    




    # Ручной поиск с помощью Q

    # words_for_search = [word for word in query.split() if len(word) >= 3]

    # q_object = Q()

    # for word in words_for_search:
    #     q_object |= Q(description__icontains=word)
    #     q_object |= Q(name__icontains=word)
    #     print(word)

    # return Products.objects.filter(q_object)