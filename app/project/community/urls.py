from django.urls import path

from . import views

app_name = "community"

urlpatterns = [
    path("", views.connect, name="connect"),
    path("feed/", views.feed, name="feed"),
    path("profile/", views.profile, name="profile"),
    path("user/<int:user_profile_id>", views.user, name="user"),
    path("user/<int:user_profile_id>/", views.user, name="user"),
    path("toggle-like/<int:post_id>", views.toggle_like, name="toggle-like"),
    path("toggle-follow/<int:user_profile_id>",
         views.toggle_follow, name="toggle-follow"),
    path("get-like-info/<int:post_id>",
         views.get_like_info, name="get-like-info"),
    # path("post-comment/<int:post_id>", views.post_comment, name="post-comment"),
]
