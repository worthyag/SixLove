from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

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
        print(request.POST)  # testing

        post_id = request.POST.get("post-id")

        if post_id == "create":
            # Creating a new post.
            form = forms.UserPostsForm(request.POST, request.FILES)

            if form.is_valid():
                post = form.save(commit=False)

                try:
                    user_profile = models.UserProfile.objects.get(
                        user=request.user)
                    post.user_profile = user_profile
                    post.save()
                except models.UserProfile.DoesNotExist:
                    print("User profile does not exist.")

                return redirect("community:feed")
            else:
                return HttpResponseBadRequest("Invalid form data")

        elif post_id == "edit":
            # Editing the post.
            try:
                selected_post = get_object_or_404(models.UserPosts,
                                                  id=int(
                                                      request.POST["post-id-to-edit"])
                                                  )
            except:
                return HttpResponseBadRequest("Invalid request")

            # Creating a form instance with the provided data and the
            # instance to be updated.
            form = forms.UserPostsForm(request.POST,
                                       request.FILES,
                                       instance=selected_post)

            if form.is_valid():
                post = form.save(commit=False)

                # Only the user who created the post can edit it.
                try:
                    user_profile = models.UserProfile.objects.get(
                        user=request.user)
                    post.user_profile = user_profile

                    # Ensure that no new picture is given.
                    post.post_picture = selected_post.post_picture
                    post.save()
                except models.UserProfile.DoesNotExist:
                    print("User profile does not exist.")

                return redirect("community:feed")
            else:
                return HttpResponseBadRequest("Invalid form data")

        elif post_id == "delete":
            # Deleting a post.
            try:
                selected_post = get_object_or_404(models.UserPosts,
                                                  id=int(
                                                      request.POST["post-id-to-delete"])
                                                  )
            except:
                return HttpResponseBadRequest("Invalid request")

            # Only the user who created the post can delete it.
            try:
                user_profile = models.UserProfile.objects.get(
                    user=request.user)

                if user_profile and selected_post.user_profile == user_profile:
                    selected_post.delete()
                    return redirect("community:feed")

            except models.UserProfile.DoesNotExist:
                print("User profile does not exist.")

        else:
            pass
    else:
        # Initialising a new form.
        form = forms.UserPostsForm()

    try:
        user_profile = models.UserProfile.objects.get(user=request.user)
        following_users = user_profile.following.all()

        # Get posts from user's profile and users they are following.
        following_posts = models.UserPosts.objects.filter(
            user_profile__in=following_users) | models.UserPosts.objects.filter(
            user_profile=user_profile)
        following_posts = following_posts.order_by('-created_at').distinct()
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
    # First checking whether a user profile exists.
    try:
        user_profile = models.UserProfile.objects.get(user=request.user)
        user_posts = models.UserPosts.objects.filter(
            user_profile=user_profile).order_by('-created_at')

    except models.UserProfile.DoesNotExist:
        user_profile = None
        user_posts = None

    # If a user profile does not exist.
    if not user_profile:
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

        return render(
            request,
            "./community/profile.html",
            {
                "title": "Profile",
                "form": form
            }
        )
    # If a user profile does exist.
    else:
        user_posts = models.UserPosts.objects.filter(
            user_profile=user_profile).order_by('-created_at')

        if request.method == 'POST':
            post_id = request.POST.get("post-id")

            if post_id == "edit":
                # Editing the post.
                try:
                    selected_post = get_object_or_404(models.UserPosts,
                                                      id=int(
                                                          request.POST["post-id-to-edit"])
                                                      )
                except:
                    return HttpResponseBadRequest("Invalid request")

                # Creating a form instance with the provided data and the
                # instance to be updated.
                form = forms.UserPostsForm(request.POST,
                                           request.FILES,
                                           instance=selected_post)

                if form.is_valid():
                    post = form.save(commit=False)

                    # Only the user who created the post can edit it.
                    try:
                        user_profile = models.UserProfile.objects.get(
                            user=request.user)
                        post.user_profile = user_profile

                        # Ensure that no new picture is given.
                        post.post_picture = selected_post.post_picture
                        post.save()
                    except models.UserProfile.DoesNotExist:
                        print("User profile does not exist.")

                    return redirect("community:feed")
                else:
                    return HttpResponseBadRequest("Invalid form data")

            elif post_id == "delete":
                # Deleting a post.
                try:
                    selected_post = get_object_or_404(models.UserPosts,
                                                      id=int(
                                                          request.POST["post-id-to-delete"])
                                                      )
                except:
                    return HttpResponseBadRequest("Invalid request")

                # Only the user who created the post can delete it.
                try:
                    user_profile = models.UserProfile.objects.get(
                        user=request.user)

                    if user_profile and selected_post.user_profile == user_profile:
                        selected_post.delete()
                        return redirect("community:feed")

                except models.UserProfile.DoesNotExist:
                    print("User profile does not exist.")

            else:
                pass
        else:
            # Initialising a new form.
            form = forms.UserPostsForm()

        try:
            following_users = user_profile.following.all()

            # Get posts from user's profile and users they are following.
            following_posts = models.UserPosts.objects.filter(
                user_profile__in=following_users) | models.UserPosts.objects.filter(
                user_profile=user_profile)
            following_posts = following_posts.order_by(
                '-created_at').distinct()
        except:
            following_posts = None

        return render(
            request,
            "./community/profile.html",
            {
                "title": "Profile",
                "user_profile": user_profile,
                "user_posts": user_posts,
                "form": form
            }
        )

    # if request.method == 'POST':
    #     form = forms.UserProfileForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         user_profile = form.save(commit=False)
    #         user_profile.user = request.user
    #         user_profile.save()
    #         return redirect("community:profile")
    # else:
    #     # Initialising a new form.
    #     form = forms.UserProfileForm()

    # try:
    #     user_profile = models.UserProfile.objects.get(user=request.user)
    #     user_posts = models.UserPosts.objects.filter(
    #         user_profile=user_profile).order_by('-created_at')

    # except models.UserProfile.DoesNotExist:
    #     user_profile = None
    #     user_posts = None

    # if user_profile:
    #     user_posts = models.UserPosts.objects.filter(
    #         user_profile=user_profile).order_by('-created_at')
    #     return render(
    #         request,
    #         "./community/profile.html",
    #         {
    #             "title": "Profile",
    #             "user_profile": user_profile,
    #             "user_posts": user_posts,
    #         }
    #     )
    # else:
    #     # If there is no profile, render the template without user_profile and user_posts
    #     return render(
    #         request,
    #         "./community/profile.html",
    #         {
    #             "title": "Profile",
    #             "form": form
    #         }
    #     )
