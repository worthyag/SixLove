from django.urls import path

from . import views

app_name = "community"

urlpatterns = [
    path("", views.connect, name="connect"),
    path("feed/", views.feed, name="feed"),
    path("profile/", views.profile, name="profile"),
]
