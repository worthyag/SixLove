from django.shortcuts import render

# Create your views here.


def home(request):
    return render(
        request,
        "./registration/index.html",
        {
            "title": "Home"
        }
    )


def user_login(request):
    return render(
        request,
        "./registration/login.html",
        {
            "title": "Login"
        }
    )


def signup(request):
    return render(
        request,
        "./registration/signup.html",
        {
            "title": "Sign Up"
        }
    )


def onboarding(request):
    return render(
        request,
        "./registration/onboarding.html",
        {
            "title": "Onboarding"
        }
    )
