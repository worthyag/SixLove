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
    # user_profile, created = models.UserProfile.objects.get_or_create(
    #     user=request.user)

    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect("community:profile")
    else:
        # Initialising a new form.
        form = forms.UserProfileForm()

    try:
        user_profile = models.UserProfile.objects.get(user=request.user)
        user_posts = models.UserPosts.objects.filter(
            user_profile=user_profile).order_by('-created_at')

    except models.UserProfile.DoesNotExist:
        user_profile = None
        user_posts = None

    if user_profile:
        user_posts = models.UserPosts.objects.filter(
            user_profile=user_profile).order_by('-created_at')
        return render(
            request,
            "./community/profile.html",
            {
                "title": "Profile",
                "user_profile": user_profile,
                "user_posts": user_posts,
            }
        )
    else:
        # If there is no profile, render the template without user_profile and user_posts
        return render(
            request,
            "./community/profile.html",
            {
                "title": "Profile",
                "form": form
            }
        )

    # try:
    #     user_profile = models.UserProfile.objects.get(user=request.user)
    #     user_posts = models.UserPosts.objects.filter(
    #         user=request.user).order_by('-created_at')
    # except:
    #     user_profile = None
    #     user_posts = None

    # return render(
    #     request,
    #     "./community/profile.html",
    #     {
    #         "title": "Profile",
    #         "user_profile": user_profile,
    #         "user_posts": user_posts,
    #         "form": form
    #     }
    # )
