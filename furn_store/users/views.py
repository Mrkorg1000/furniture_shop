from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.urls import reverse


# Create your views here.
def login(request) -> HttpResponse:
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))

    else:
        form = UserLoginForm()
    context = {
        "title": "Home - Авторизация",
        "form": form,
    }
    return render(request, 'users/login.html', context)


def registration(request) -> HttpResponse:
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))

    else:
        form = UserRegistrationForm()
    context = {
        "title": "Home - Регистрация",
        "form": form,
    }
    return render(request, "users/registration.html", context)


@login_required
def profile(request) -> HttpResponse:
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))

    else:
        form = ProfileForm(instance=request.user)
    context = {
        "title": "Home - Кабинет",
        "form": form,
    }
    return render(request, "users/profile.html", context)

@login_required
def logout(request) -> HttpResponse:
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)

    return redirect(reverse("main:index"))
