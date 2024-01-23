from django.shortcuts import render

# Create your views here.


def landing(request, *args, **kwargs):
    return render(request, "landing.html")


def login(request, *args, **kwargs):
    return render(request, "login.html")


def signup(request, *args, **kwargs):
    return render(request, "signup.html")


def tennis(request, *args, **kwargs):
    return render(request, "tennis.html", {
        "use_bootstrap": True
    })


def feed(request, *args, **kwargs):
    return render(request, "feed.html", {
        "use_bootstrap": True
    })


def learn(request, *args, **kwargs):
    return render(request, "learn.html", {
        "use_bootstrap": True
    })


def history(request, *args, **kwargs):
    return render(request, "history.html")


def profile(request, *args, **kwargs):
    return render(request, "profile.html", {
        "page": "profile",
        "use_bootstrap": True
    })
