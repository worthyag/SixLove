from datetime import datetime, timedelta
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponseBadRequest


# from .utils import TennisCalendar

from tennis import models as TennisModels
from tennis import forms as TennisForms

# Create your views here.


@login_required
def calendar(request):
    """"""
    tennis_sessions = TennisModels.TennisSession.objects.filter(
        user=request.user
    )

    # Convert the QuerySet to a list of dictionaries
    tennis_sessions_data = [{'title': session.title, 'date': session.date.strftime("%Y-%m-%d"),
                             'notes': session.notes, 'isCompleted': str(session.is_completed), 'id': session.id} for session in tennis_sessions]

    json_data = json.dumps(tennis_sessions_data)

    if request.method == "POST":
        print(request.POST)
        if (request.POST["session-id"] != "X"):
            try:
                selected_session = get_object_or_404(TennisModels.TennisSession,
                                                     id=int(
                                                         request.POST["session-id"]),
                                                     user=request.user)
            except:
                return HttpResponseBadRequest("Invalid request")
            form = TennisForms.TennisSessionForm(request.POST,
                                                 instance=selected_session)

            if form.is_valid():
                form.save()
                return redirect("planner:calendar")
            else:
                return HttpResponseBadRequest("Invalid form data")
        else:
            form = TennisForms.TennisSessionForm(request.POST)

            if form.is_valid():
                session = form.save(commit=False)
                session.user = request.user
                session.save()
                return redirect("planner:calendar")
            else:
                return HttpResponseBadRequest("Invalid form data")
    else:
        # Initialising a new form.
        form = TennisForms.TennisSessionForm()

    return render(
        request,
        "./planner/calendar.html",
        {
            "title": "Calendar",
            "tennis_sessions": json_data,
            "form": form
        }
    )
