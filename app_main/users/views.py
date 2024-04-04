from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                messages.success(request=request, message=f"{username}, вы вошли в свой аккаунт.")

                if request.POST.get("next", None):
                    return HttpResponseRedirect(request.POST.get("next"))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {"title": "Авторизация", "form": form}
    return render(request, "users/login.html", context)



def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(user=user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {"title": "Регистрация", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {"title": "Кабинет", "form": form}
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    messages.warning(request=request, message="Вы вышли из аккаунта.")
    auth.logout(request=request)
    return HttpResponseRedirect(reverse('user:login'))


def users_basket(request):
    context = {"title": "Корзина"}
    return render(request, "users/user-cart.html", context)