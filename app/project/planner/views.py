from datetime import datetime, timedelta
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
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

    # Serialising the date field to a string before passing it to the template.
    # json_tennis_sessions = json.dumps(
    #     list(tennis_sessions.values()), cls=DjangoJSONEncoder)
    # json_tennis_sessions = json.dumps(tennis_sessions, cls=DjangoJSONEncoder)

    tennis_sessions_str = [
        {
            "title": "test",
            "notes": "notes here",
            "date": timezone.now().date(),
            "isCompleted": False
        }
    ]
    json_tennis_sessions = json.dumps(
        tennis_sessions_str, cls=DjangoJSONEncoder)

    return render(
        request,
        "./planner/calendar.html",
        {
            "title": "Calendar",
            'tennis_sessions': json_tennis_sessions
        }
    )
