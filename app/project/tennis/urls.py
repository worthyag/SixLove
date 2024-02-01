from django.urls import path

from . import views

app_name = "tennis"

urlpatterns = [
    path("", views.tennis, name="tennis"),
    path("add/", views.add, name="add"),
]
