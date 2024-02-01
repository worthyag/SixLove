from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("onboarding/", views.onboarding, name="onboarding"),
    path("tennis/", views.tennis, name="tennis"),
    path("feed/", views.feed, name="feed"),
    path("learn/", views.learn, name="learn"),
    path("history/", views.history, name="history"),
    path("profile/", views.profile, name="profile"),
]
