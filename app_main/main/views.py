from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": "Home",
        "content": "Pizza House HOME"
    }
    return render(request=request, template_name='main/index.html', context=context)


def about(request):
    return HttpResponse("Page about")






