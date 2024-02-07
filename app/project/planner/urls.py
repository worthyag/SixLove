from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "planner"

urlpatterns = [
    # path("", views.calendar, name="calendar"),
    path("", login_required(views.CalendarView.as_view()), name="calendar"),
    # path("<int:year>/<int:month>/", views.calendar, name="calendar"),
]
