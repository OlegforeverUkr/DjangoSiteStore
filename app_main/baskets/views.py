from django.http import HttpResponse
from django.shortcuts import render

def basket_add(request, product_id):
    return HttpResponse("basket_add")


def basket_change(request, product_id):
    return HttpResponse("basket_change")


def basket_remove(request, product_id):
    return HttpResponse("basket_remove")
