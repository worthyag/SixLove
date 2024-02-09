from datetime import datetime, timedelta
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse

# from .utils import TennisCalendar

from tennis import models as TennisModels

# Create your views here.


@login_required
def calendar(request, year=None, month=None):
    """"""
    tennis_sessions = TennisModels.TennisSession.objects.filter(
        user=request.user
    )

    # Convert the QuerySet to a list of dictionaries
    tennis_sessions_data = [{'title': session.title, 'date': session.date.strftime("%Y-%m-%d"),
                             'notes': session.notes, 'isCompleted': str(session.is_completed)} for session in tennis_sessions]

    json_data = json.dumps(tennis_sessions_data)

    return render(
        request,
        "./planner/calendar.html",
        {
            "title": "Calendar",
            'tennis_sessions': json_data,
        }
    )
