from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def landing(request, *args, **kwargs):
    return render(request, "landing.html")


def tennis(request, *args, **kwargs):
    return render(request, "tennis.html")
