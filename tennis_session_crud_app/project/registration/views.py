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
                  {
                      "title": "Sign Up",
                      "form": form
                  }
                  )


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("tennis-sessions")
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
