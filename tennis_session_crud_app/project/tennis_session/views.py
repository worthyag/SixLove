from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse

from . import forms
from . import models

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = forms.TennisSessionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        # Initialising a new form.
        form = forms.TennisSessionForm()

    return render(
        request,
        "./tennis_session/index.html",
        {
            "title": "Tennis Session",
            "form": form,
        }
    )


def success(request):
    return render(
        request,
        "./tennis_session/success.html",
        {
            "title": "Success"
        })


def view_sessions(request):
    tennis_sessions = models.TennisSession.objects.all()

    return render(
        request,
        "./tennis_session/view_sessions.html",
        {
            "title": "View Sessions",
            "tennis_sessions": tennis_sessions
        })


def edit_session(request, tennis_session_id):
    selected_session = get_object_or_404(models.TennisSession,
                                         id=tennis_session_id)

    if request.method == "POST":
        form = forms.TennisSessionForm(request.POST,
                                       instance=selected_session)

        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = forms.TennisSessionForm(instance=selected_session)

    return render(
        request,
        "./tennis_session/edit_session.html",
        {
            "title": "Edit Session",
            "form": form
        })
