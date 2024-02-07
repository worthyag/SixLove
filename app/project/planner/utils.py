from datetime import datetime, timedelta
from calendar import HTMLCalendar
# import itertools

# from django.utils import timezone

from tennis import models as TennisModels


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
        sessions_per_day = tennis_sessions.filter(
            user=self.user, date__day=day)
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
        tennis_sessions = TennisModels.TennisSession.objects.filter(
            user=self.user,
            date__year=self.year,
            date__month=self.month,
        )

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year,
                                       self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'

        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, tennis_sessions)}\n'
        return cal
