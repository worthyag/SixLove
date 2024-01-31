from django.urls import path
from . import views

app_name = "user_auth"

urlpatterns = [
    path("login/", views.login, name="login")
]
