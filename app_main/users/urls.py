from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('login/', view=views.login, name='login'),
    path('registration/', view=views.registration, name='registration'),
    path('profile/', view=views.profile, name='profile'),
    path('logout/', view=views.logout, name='logout'),
    path('users-basket/', view=views.users_basket, name='users_basket'),
]