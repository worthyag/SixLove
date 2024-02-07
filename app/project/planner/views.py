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

    def formatday(self, day, weekday):
        """"""
        if day != 0:
            cssclass = self.cssclasses[weekday]

            if timezone.now().date() == datetime(self.year, self.month, day).date():
                cssclass += " today"
            if day in self.tennis_sessions:
                cssclass += " filled"
                body = ['<ul class="tennis_session">']
                for tennis_session in self.tennis_sessions[day]:
                    body.append(f"<li>{tennis_session.title}</li>")
                body.append("</ul>")
                return self.day_cell(cssclass, f'<span class="day-number">{day}</span> {"".join(body)}')
            return self.day_cell(cssclass, f'<span class="day-number">{day}</span>')
        return self.day_cell("noday", "&nbsp;")

    def formatmonth(self, year, month, withyear=True):
        """"""
        self.year, self.month = year, month
        return super(TennisCalendar, self).formatmonth(year, month, withyear)

    def group_by_day(self, tennis_sessions):
        """"""
        def field(tennis_session): return tennis_session.start_time.day
        return {day: list(items) for day, items in groupby(tennis_sessions, field)}

    def day_cell(self, cssclass, body):
        """"""
        return f'<td class="{cssclass}">{body}</td>'


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
