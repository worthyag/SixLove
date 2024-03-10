from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, authenticate

from tennis import models as TennisModels

from .forms import CustomUserCreationForm
# Create your views here.


def home(request):
    """"""
    tennis_sessions = TennisModels.TennisSession.objects.filter(
        user=request.user
    )

    forehand_sessions = [
        session for session in tennis_sessions if session.category == "forehand"]
    backhand_sessions = [
        session for session in tennis_sessions if session.category == "backhand"]
    serve_sessions = [
        session for session in tennis_sessions if session.category == "serve"]
    volley_sessions = [
        session for session in tennis_sessions if session.category == "volley"]
    slice_sessions = [
        session for session in tennis_sessions if session.category == "slice"]
    smash_sessions = [
        session for session in tennis_sessions if session.category == "smash"]

    return render(
        request,
        "./registration/index.html",
        {
            "title": "Home",
            "tennis_sessions": tennis_sessions,
            "forehand_sessions": forehand_sessions,
            "backhand_sessions": backhand_sessions,
            "serve_sessions": serve_sessions,
            "volley_sessions": volley_sessions,
            "slice_sessions": slice_sessions,
            "smash_sessions": smash_sessions,
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


# def onboarding(request):
#     """"""
#     return render(
#         request,
#         "./registration/onboarding.html",
#         {
#             "title": "Onboarding"
#         }
#     )


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
