from django.urls import path
from . import views

app_name = ""

urlpatterns = [
    path("", views.index, name="index"),
    path("success/", views.success, name="success"),
    path("tennis-sessions/", views.view_sessions, name="tennis-sessions"),
    path("tennis-sessions/<int:tennis_session_id>/edit",
         views.edit_session, name="edit-tennis-session"),
]
