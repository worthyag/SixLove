from django.urls import path

from . import views

app_name = "planner"

urlpatterns = [
    path("", views.calendar, name="calendar"),
    # path("ajax_calendar/", views.ajax_calendar, name="ajax_calendar"),
]
