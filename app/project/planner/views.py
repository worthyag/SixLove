from calendar import HTMLCalendar
from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.


class TennisCalendar(HTMLCalendar):
    """"""

    def __init__(self, tennis_sessions):
        super(TennisCalendar, self).__init__()
        self.tennis_sessions = self.group_by_day(tennis_sessions)

    def format_day(self, day, weekday):
        """"""
        if day != 0:
            css_class = self.cssclasses[weekday]

            if timezone.now().date() == datetime(self.year, self.month, day).date():
                css_class += " today"


@login_required
def calendar(request):
    """"""
    return render(
        request,
        "./planner/calendar.html",
        {
            "title": "Calendar",
        }
    )
