from django.urls import path
from . import views

app_name = ""

urlpatterns = [
    path("", views.index, name="index"),
    path("success/", views.success, name="success"),
    path("tennis-sessions/", views.view_tennis_sessions, name="tennis-sessions"),
    path("tennis-sessions/<int:tennis_session_id>/edit",
         views.edit_tennis_session, name="edit-tennis-session"),
    path("tennis-sessions/<int:tennis_session_id>/delete",
         views.delete_tennis_session, name="delete-tennis-session"),
    path("calendar", views.calendar, name="calendar"),
]
