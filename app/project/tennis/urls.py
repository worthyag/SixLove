from django.urls import path

from . import views

app_name = "tennis"

urlpatterns = [
    path("", views.tennis, name="tennis"),
    path("add/", views.add, name="add"),
    path("<int:tennis_session_id>/edit/",
         views.edit_tennis_session, name="edit"),
    path("<int:tennis_session_id>/delete/",
         views.delete_tennis_session, name="delete"),
    path("success/", views.success, name="success"),
    path("learn/", views.learn, name="learn"),
]
