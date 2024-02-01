from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("You have reached the home page.")


def user_login(request):
    return HttpResponse("You have reached the login page.")


def signup(request):
    return HttpResponse("You have reached the signup page.")


def onboarding(request):
    return HttpResponse("You have reached the onboarding page.")
