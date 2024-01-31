from django.urls import path
from . import views

app_name = ""

urlpatterns = [
    path("", views.index, name="index"),
    path("success/", views.success, name="success"),
    path("view_sessions/", views.view_sessions, name="view_sessions"),
]
