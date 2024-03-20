from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.index, name='index'),
    path('about/', view=views.about, name='about'),
]
