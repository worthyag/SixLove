from django.urls import path

from . import views

app_name = "community"

urlpatterns = [
    path("", views.connect, name="connect"),
    path("feed/", views.feed, name="feed"),
    path("profile/", views.profile, name="profile"),
    path("toggle-like/<int:post_id>", views.toggle_like, name="toggle-like"),
    path("get-like-info/<int:post_id>",
         views.get_like_info, name="get-like-info"),
]
