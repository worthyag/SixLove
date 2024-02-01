import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from . import forms
from . import models


# Create your views here.

def tennis(request):
    """"""
    # tennis_sessions = models.TennisSession.objects.filter(
    #     user=request.user).order_by("date")

    # today_sessions = [
    #     session for session in tennis_sessions if session.is_tennis_session_scheduled_today()]
    # is_today = "No sessions scheduled for today." if len(
    #     today_sessions) == 0 else ""

    # upcoming_sessions = [session for session in tennis_sessions
    #                      if not session.is_tennis_session_scheduled_today() and
    #                      session.date > datetime.date.today()]

    # past_sessions = [session for session in tennis_sessions
    #                  if not session.is_tennis_session_scheduled_today() and
    #                  session.date < datetime.date.today()]

    # return render(
    #     request,
    #     "./tennis/tennis.html",
    #     {
    #         "title": "Tennis",
    #         "today_sessions": today_sessions,
    #         "is_today": is_today,
    #         "upcoming_sessions": upcoming_sessions,
    #         "past_sessions": past_sessions,
    #     })

    return render(
        request,
        "./tennis/tennis.html",
        {
            "title": "Tennis",
            # "today_sessions": today_sessions,
            # "is_today": is_today,
            # "upcoming_sessions": upcoming_sessions,
            # "past_sessions": past_sessions,
        })


def add(request):
    """"""
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
        "./tennis/add_tennis_session.html",
        {
            "title": "Add Tennis Session",
            "form": form,
        }
    )
