from calendar import HTMLCalendar
from datetime import datetime, timedelta
import itertools

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from tennis import models as TennisModels

# Create your views here.


# class TennisCalendar(HTMLCalendar):
#     """"""

#     def __init__(self, year=None, month=None, tennis_sessions=None):
#         self.year = year
#         self.month = month
#         self.tennis_sessions = tennis_sessions
#         super(TennisCalendar, self).__init__()

#     def formatday(self, day, weekday):
#         """"""
#         if day != 0:
#             cssclass = self.cssclasses[weekday]
#             items = self.tennis_sessions_per_day(day)

#             if timezone.now().date() == datetime(self.year, self.month, day).date():
#                 cssclass += " today"
#             if items:
#                 cssclass += " filled"
#                 body = ['<ul class="day_ul">']

#                 for item in items:
#                     body.append(f"<li>{item.title}</li>")
#                 body.append("</ul>")

#                 return self.day_cell(cssclass, f'<span class="day_num">{day}</span> {"".join(body)}')

#             return self.day_cell(cssclass, f'<span class="day_num">{day}</span>')

#         return self.day_cell("noday", "&nbsp;")

#     # def formatmonth(self, year, month, withyear=True):
#     #     """"""
#     #     self.year, self.month = year, month
#     #     return super(TennisCalendar, self).formatmonth(year, month, withyear)

#     # def group_by_day(self, tennis_sessions):
#     #     """"""
#     #     def field(tennis_session): return tennis_session.start_time.day
#     #     return {day: list(items) for day, items in itertools.groupby(tennis_sessions, field)}

#     def day_cell(self, cssclass, body):
#         """"""
#         return f'<td class="{cssclass}">{body}</td>'

#     def tennis_sessions_per_day(self, day):
#         """Return all tennis sessions for a particular day."""
#         field = lambda tennis_session: tennis_session.date.day if type(tennis_session.date) != type("") else tennis_session.date[8:11]

#         return {tennis_session.title: list(items) for tennis_session, items in itertools.groupby(self.tennis_sessions, field)}


class TennisCalendar(HTMLCalendar):
    """"""

    def __init__(self, year=None, month=None, user=None):
        """"""
        self.year = year
        self.month = month
        self.user = None
        super(TennisCalendar, self).__init__()

    def formatdate(self, day, tennis_sessions):
        """
        Formats a day as a td. Filters events by day.
        """
        sessions_per_day = tennis_sessions.filter(date__day=day)
        d = ""

        for session in sessions_per_day:
            d += f'<li> {session.title} </li>'

        if day != 0:
            return f'<td><span class="date">{day}</span><ul> {d} </ul></td>'
        return f'<td></td>'

    def formatweek(self, theweek, tennis_sessions):
        """
        Formats a week as a tr.
        """
        week = ""

        for d, weekday in theweek:
            week += self.formatdate(d, tennis_sessions)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        """
        Formats a month as a table. Filters events by year and month.
        """
        tennis_sessions = TennisModels.TennisSession.objects.filter()

        for d, weekday in theweek:
            week += self.formatdate(d, tennis_sessions)
        return f'<tr> {week} </tr>'


@login_required
def calendar(request, year=None, month=None):
    """"""
    tennis_sessions = TennisModels.TennisSession.objects.filter(
        user=request.user
    )
    cal = TennisCalendar(tennis_sessions)

    month, year = month if month else timezone.now().date(
    ).month, year if year else timezone.now().date().year

    # Assuming you have a method to convert your TennisSession objects into a format suitable for the calendar
    tennis_sessions = [
        {
            'title': tennis_session.title,
            'day': tennis_session.date.day if type(tennis_session.date) != type("") else tennis_session.date[8:11]
        } for tennis_session in tennis_sessions]

    # html_cal = cal.formatmonth(int(year), int(month), withyear=True, tennis_sessions=tennis_sessions)

    return render(
        request,
        "./planner/calendar.html",
        {
            "title": "Calendar",
            "year": year,
            "month": month,
            "calendar": cal,
            'tennis_sessions': tennis_sessions
        }
    )
