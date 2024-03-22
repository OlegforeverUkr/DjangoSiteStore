from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path('', view=views.catalog, name='index'),
    path('product/', view=views.product, name='product'),
]