from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, authenticate

from .forms import CustomUserCreationForm
# Create your views here.


def home(request):
    """"""
    return render(
        request,
        "./registration/index.html",
        {
            "title": "Home"
        }
    )


def signup(request):
    """"""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(
        request,
        "./registration/signup.html",
        {
            "title": "Sign Up",
            "form": form
        }
    )


def onboarding(request):
    """"""
    return render(
        request,
        "./registration/onboarding.html",
        {
            "title": "Onboarding"
        }
    )


def user_login(request):
    """"""
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(
        request,
        "./registration/login.html",
        {
            "title": "Login",
            "form": form
        }
    )