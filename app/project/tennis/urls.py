from django.urls import path

from . import views

app_name = "tennis"

urlpatterns = [
    path("", views.tennis, name="tennis"),
    path("add/", views.add, name="add"),
    path("<int:tennis_session_id>/edit/", views.add, name="edit"),
    path("<int:tennis_session_id>/delete/", views.add, name="delete"),
    path("success/", views.add, name="success"),
]
