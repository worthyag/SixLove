from django.urls import path

from . import views

app_name = "planner"

urlpatterns = [
    # path("", views.calendar, name="calendar"),
    path("", views.CalendarView.as_view(), name="calendar"),
    # path("<int:year>/<int:month>/", views.calendar, name="calendar"),
]
