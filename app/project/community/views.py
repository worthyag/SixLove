from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import models

# Create your views here.


@login_required
def connect(request):
    """"""
    return render(
        request,
        "./community/connect.html",
        {
            "title": "Connect",
        }
    )


@login_required
def feed(request):
    """"""
    return render(
        request,
        "./community/feed.html",
        {
            "title": "Feed",
        }
    )


@login_required
def profile(request):
    """"""
    try:
        user_profile = models.UserProfile.objects.get(user=request.user)
        user_posts = models.UserPosts.objects.filter(
            user=request.user).order_by('-created_at')
    except:
        user_profile = None
        user_posts = None

    return render(
        request,
        "./community/profile.html",
        {
            "title": "Profile",
            "user_profile": user_profile,
            "user_posts": user_posts
        }
    )
