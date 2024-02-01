from django.urls import path
from . import views

app_name = ""

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("onboarding/", views.onboarding, name="onboarding"),
]
