from django.shortcuts import render

# Create your views here.


def connect(request):
    render(
        request,
        "./community/connect.html",
        {
            "title": "Connect",
        }
    )
