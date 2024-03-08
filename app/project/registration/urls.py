from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = ""

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    # path("onboarding/", views.onboarding, name="onboarding"),
    path("login/", views.user_login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
