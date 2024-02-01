from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def tennis(request):
    return render(
        request,
        "./tennis/tennis.html",
        {
            "title": "Tennis"
        }
    )
