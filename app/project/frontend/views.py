from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def landing(request, *args, **kwargs):
    return render(request, "landing.html")


def login(request, *args, **kwargs):
    return render(request, "login.html")


def signup(request, *args, **kwargs):
    return render(request, "signup.html")


def tennis(request, *args, **kwargs):
    return render(request, "tennis.html")


def feed(request, *args, **kwargs):
    return render(request, "feed.html")


def learn(request, *args, **kwargs):
    return render(request, "learn.html")


def history(request, *args, **kwargs):
    return render(request, "history.html")


def profile(request, *args, **kwargs):
    return render(request, "profile.html")
