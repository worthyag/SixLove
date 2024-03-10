from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.db.models import Exists, OuterRef, Q, Count, Max, F

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

    # To allow the user to pick the chart they want to see.
    filter_option = request.GET.get("filter", "")

    # Applying filters based on the filter_option.
    if filter_option == "completed":
        tennis_sessions = tennis_sessions.filter(
            is_completed=True)

    elif filter_option == "not_completed":
        tennis_sessions = tennis_sessions.filter(
            is_completed=False)

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
    drop_shot_sessions = [
        session for session in tennis_sessions if session.category == "drop-shot"]
    agility_sessions = [
        session for session in tennis_sessions if session.category == "agility"]
    stamina_sessions = [
        session for session in tennis_sessions if session.category == "stamina"]
    other_sessions = [
        session for session in tennis_sessions if session.category == "other"]

    return render(
        request,
        "./registration/index.html",
        {
            "title": "Home",
            "tennis_sessions": tennis_sessions,
            "filter_option": filter_option,
            "forehand_sessions": forehand_sessions,
            "backhand_sessions": backhand_sessions,
            "serve_sessions": serve_sessions,
            "volley_sessions": volley_sessions,
            "slice_sessions": slice_sessions,
            "smash_sessions": smash_sessions,
            "drop_shot_sessions": drop_shot_sessions,
            "agility_sessions": agility_sessions,
            "stamina_sessions": stamina_sessions,
            "other_sessions": other_sessions,
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
