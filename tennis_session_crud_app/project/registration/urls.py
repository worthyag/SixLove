from django.urls import path

from . import views

app_name = "registration"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("signup/", views.signup, name="signup"),
]
