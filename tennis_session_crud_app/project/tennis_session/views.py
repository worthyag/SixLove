from django.shortcuts import render, redirect
# from django.http import HttpResponse

from . import forms

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = forms.AddTennisSessionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")

    # Initialising a new form.
    form = forms.AddTennisSessionForm()

    return render(
        request,
        "./tennis_session/index.html",
        {
            "title": "Tennis Session",
            "form": form,
        }
    )


def success(request):
    return render(request, "./tennis_session/success.html")
