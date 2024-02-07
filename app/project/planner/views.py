from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import generic
from django.utils.safestring import mark_safe

from .utils import TennisCalendar

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


# @login_required
class CalendarView(generic.ListView):
    """"""
    model = TennisModels.TennisSession
    template_name = "./planner/calendar.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.user = request.user

    def get_context_date(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)

        # Using today's date for the calendar.
        today = get_date(self.request.GET.get('day', None))

        # Instantiating the tennis calendar class with today's year and date.
        cal = TennisCalendar(today.year, today.month, self.user)

        # Calling the formatmonth method, which returns our calendar as a table.
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    """"""
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return timezone.now().date()


# @login_required
# def calendar(request, year=None, month=None):
#     """"""
#     tennis_sessions = TennisModels.TennisSession.objects.filter(
#         user=request.user
#     )
#     cal = TennisCalendar(tennis_sessions, user=request.user)

#     month, year = month if month else timezone.now().date(
#     ).month, year if year else timezone.now().date().year

#     # Assuming you have a method to convert your TennisSession objects into a format suitable for the calendar
#     tennis_sessions = [
#         {
#             'title': tennis_session.title,
#             'day': tennis_session.date.day if type(tennis_session.date) != type("") else tennis_session.date[8:11]
#         } for tennis_session in tennis_sessions]

#     # html_cal = cal.formatmonth(int(year), int(month), withyear=True, tennis_sessions=tennis_sessions)

#     return render(
#         request,
#         "./planner/calendar.html",
#         {
#             "title": "Calendar",
#             "year": year,
#             "month": month,
#             "calendar": cal,
#             'tennis_sessions': tennis_sessions
#         }
#     )
