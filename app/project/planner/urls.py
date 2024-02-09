from django.urls import path

from . import views

app_name = "planner"

urlpatterns = [
    path("", views.calendar, name="calendar"),
    path("<int:id>", views.calendar, name="calendar"),
]
