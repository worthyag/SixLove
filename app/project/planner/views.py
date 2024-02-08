from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# from django.utils.safestring import mark_safe

# from .utils import TennisCalendar

from tennis import models as TennisModels


# Create your views here.


@login_required
def calendar(request, year=None, month=None):
    """"""
    tennis_sessions = TennisModels.TennisSession.objects.filter(
        user=request.user
    )

    return render(
        request,
        "./planner/calendar.html",
        {
            "title": "Calendar",
            'tennis_sessions': tennis_sessions
        }
    )
