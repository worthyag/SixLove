from django.shortcuts import render

# Create your views here.


def connect(request):
    """"""
    return render(
        request,
        "./community/connect.html",
        {
            "title": "Connect",
        }
    )


def feed(request):
    """"""
    return render(
        request,
        "./community/feed.html",
        {
            "title": "Feed",
        }
    )


def profile(request):
    """"""
    return render(
        request,
        "./community/profile.html",
        {
            "title": "Profile",
        }
    )
