from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

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
    if request.method == 'POST':
        form = forms.UserPostsForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile.user = request.user
            post.save()
            return redirect("community:feed")
    else:
        # Initialising a new form.
        form = forms.UserPostsForm()

    try:
        user_profile = models.UserProfile.objects.get(user=request.user)
        following_users = user_profile.following.all()
        following_posts = models.UserPosts.objects.filter(
            user_profile__in=following_users).order_by('-created_at')
    except:
        user_profile = None
        following_posts = None

    return render(
        request,
        "./community/feed.html",
        {
            "title": "Feed",
            "user_profile": user_profile,
            "posts": following_posts,
            "form": form
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
