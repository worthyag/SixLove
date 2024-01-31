from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tennis-sessions")
    else:
        form = UserCreationForm()

    return render(request,
                  "./registration/signup.html",
                  {"title": "Sign Up"}
                  )


def user_login(request):
    return render(
        request,
        "./registration/login.html",
        {"title": "Login"}
    )
