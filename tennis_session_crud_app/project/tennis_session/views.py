import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# from django.http import HttpResponse

from . import forms
from . import models

# Create your views here.


@login_required
def index(request):
    if request.method == 'POST':
        form = forms.TennisSessionForm(request.POST)

        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
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


@login_required
def success(request):
    return render(
        request,
        "./tennis_session/success.html",
        {
            "title": "Success"
        })


@login_required
def view_tennis_sessions(request):
    tennis_sessions = models.TennisSession.objects.filter(
        user=request.user).order_by("date")

    today_sessions = [
        session for session in tennis_sessions if session.is_tennis_session_scheduled_today()]
    is_today = "No sessions scheduled for today." if len(
        today_sessions) == 0 else ""

    upcoming_sessions = [session for session in tennis_sessions
                         if not session.is_tennis_session_scheduled_today() and
                         session.date > datetime.date.today()]

    past_sessions = [session for session in tennis_sessions
                     if not session.is_tennis_session_scheduled_today() and
                     session.date < datetime.date.today()]

    return render(
        request,
        "./tennis_session/view_sessions.html",
        {
            "title": "View Sessions",
            "today_sessions": today_sessions,
            "is_today": is_today,
            "upcoming_sessions": upcoming_sessions,
            "past_sessions": past_sessions,
        })


@login_required
def edit_tennis_session(request, tennis_session_id):
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


@login_required
def delete_tennis_session(request, tennis_session_id):
    selected_session = get_object_or_404(models.TennisSession,
                                         id=tennis_session_id)

    if request.method == "POST":
        selected_session.delete()
        return redirect("tennis-sessions")

    return render(
        request,
        "./tennis_session/delete_session.html",
        {
            "title": "Delete Session",
            "tennis_session": selected_session
        })


@login_required
def calendar(request):
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
        "./tennis_session/calendar.html",
        {
            "title": "Calendar",
            "form": form,
        })
