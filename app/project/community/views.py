from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.db.models import Exists, OuterRef, Q, Count, Max, F

from . import models
from . import forms

# Create your views here.


@login_required
def connect(request):
    """"""
    # Getting the profile of the request user.
    request_profile = models.UserProfile.objects.get(user=request.user)

    # To allow the user to search through the list of users.
    # Getting the search query from the request.
    query = request.GET.get("user-search", "")

    # To allow the user to filter the list of users.
    filter_option = request.GET.get("filter", "")

    # Querying the data.
    user_profiles_query = models.UserProfile.objects.filter(
        Q(username__icontains=query) | Q(profile_name__icontains=query)
    )

    # Applying additional filters based on the filter_option.
    if filter_option == "last_posted":
        user_profiles_query = user_profiles_query.annotate(
            last_posted=Max("user_posts__created_at")
        ).order_by("-last_posted")

    elif filter_option == "most_followers":
        user_profiles_query = user_profiles_query.annotate(
            follower_count=Count("followers")
        ).order_by("-follower_count")

    elif filter_option == "most_posts":
        user_profiles_query = user_profiles_query.annotate(
            post_count=Count("user_posts")
        ).order_by("-post_count")

    elif filter_option == "last_active":
        user_profiles_query = user_profiles_query.annotate(
            last_active=F("user__last_login")
        ).order_by("-last_active")

    elif filter_option == "followers":
        # Those that are following the request user.
        user_profiles_query = user_profiles_query.filter(
            following=request_profile)

    elif filter_option == "following":
        # Those that are followed by the request user.
        user_profiles_query = user_profiles_query.filter(
            followers=request_profile)

    user_profiles_data = {
        user_profile.id: {
            "username": user_profile.username,
            "profile_picture": user_profile.profile_picture.url if user_profile.profile_picture else None,
            "profile_name": user_profile.profile_name,
            "is_following": request_profile.following.filter(id=user_profile.id).exists()
        }
        # for user_profile in models.UserProfile.objects.all()
        for user_profile in user_profiles_query
    }

    request_profile_id = request_profile.id

    return render(
        request,
        "./community/connect.html",
        {
            "title": "Connect",
            "user_profiles_data": user_profiles_data,
            "search_query": query,
            "request_profile_id": request_profile_id,
            "filter_option": filter_option,
        }
    )


@login_required
def feed(request):
    """"""
    # Initialising a new form.
    form = forms.UserPostsForm()
    comment_form = forms.CommentForm()

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

        elif 'comment-submit' in request.POST:
            request_profile = models.UserProfile.objects.get(
                user=request.user)

            comment_form = forms.CommentForm(request.POST)

            if comment_form.is_valid():
                content = comment_form.cleaned_data['content']

                post = get_object_or_404(
                    models.UserPosts,
                    id=int(post_id)
                )

                post.comment(user_profile=request_profile, content=content)
                return redirect("community:feed")
            else:
                return HttpResponseBadRequest("Invalid form data")
        else:
            pass
    else:
        pass

    try:
        user_profile = models.UserProfile.objects.get(user=request.user)
        following_users = user_profile.following.all()

        # Getting the posts from user's profile and users they are following.
        following_posts = models.UserPosts.objects.filter(
            user_profile__in=following_users) | models.UserPosts.objects.filter(
            user_profile=user_profile)

        # Annotating each post with the comment count.
        following_posts = following_posts.annotate(
            comment_count=Count("comments"))

        # Annotating each post with info about whether the current user has liked it.
        following_posts = following_posts.annotate(
            user_has_liked=Exists(models.Like.objects.filter(
                user_profile=user_profile, post=OuterRef("pk")
            ))
        )

        # Ordering the posts and making sure that there are no duplicates.
        following_posts = following_posts.order_by('-created_at').distinct()

        for post in following_posts:
            if post.user_profile.username == "worthy":
                print(post.comments.all())

    except models.UserProfile.DoesNotExist:
        user_profile = None
        following_posts = None

    return render(
        request,
        "./community/feed.html",
        {
            "title": "Feed",
            "user_profile": user_profile,
            "posts": following_posts,
            "form": form,
            "comment_form": comment_form,
        }
    )


@login_required
def profile(request):
    """"""
    # Initialising a new form.
    comment_form = forms.CommentForm()

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

        # Annotating each post with info about whether the current user has liked it.
        user_posts = user_posts.annotate(
            user_has_liked=Exists(models.Like.objects.filter(
                user_profile=user_profile, post=OuterRef("pk")
            ))
        )

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

                    return redirect("community:profile")
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
                        return redirect("community:profile")

                except models.UserProfile.DoesNotExist:
                    print("User profile does not exist.")

            elif 'comment-submit' in request.POST:
                request_profile = models.UserProfile.objects.get(
                    user=request.user)

                comment_form = forms.CommentForm(request.POST)

                if comment_form.is_valid():
                    content = comment_form.cleaned_data['content']

                    post = get_object_or_404(
                        models.UserPosts,
                        id=int(post_id)
                    )

                    post.comment(user_profile=request_profile, content=content)
                    return redirect("community:profile")
                else:
                    return HttpResponseBadRequest("Invalid form data")
        else:
            # Initialising a new form.
            form = forms.UserPostsForm()

        # try:
        #     following_users = user_profile.following.all()

        #     # Get posts from user's profile and users they are following.
        #     following_posts = models.UserPosts.objects.filter(
        #         user_profile__in=following_users) | models.UserPosts.objects.filter(
        #         user_profile=user_profile)

        #     # Annotating each post with info about whether the current user has liked it.
        #     following_posts = following_posts.annotate(
        #         user_has_liked=Exists(models.Like.objects.filter(
        #             user_profile=user_profile, post=OuterRef("pk")
        #         ))
        #     )

        #     # Ordering the posts and making sure that there are no duplicates.
        #     following_posts = following_posts.order_by(
        #         '-created_at').distinct()
        # except:
        #     following_posts = None

        return render(
            request,
            "./community/profile.html",
            {
                "title": "Profile",
                "user_profile": user_profile,
                "user_posts": user_posts,
                "form": form,
                "comment_form": comment_form,
            }
        )


@login_required
def user(request, user_profile_id):
    """"""
    # Initialising a new form.
    comment_form = forms.CommentForm()

    # First checking whether a user profile exists.
    try:
        user_profile = models.UserProfile.objects.get(id=user_profile_id)
        user_posts = models.UserPosts.objects.filter(
            user_profile=user_profile).order_by('-created_at')

    except models.UserProfile.DoesNotExist:
        user_profile = None
        user_posts = None

    # If a user profile does not exist.
    if not user_profile:
        return render(
            request,
            "./community/user.html",
            {
                "title": "User Profile",
                "user_profile": user_profile,
                "user_posts": user_posts,
            }
        )
    # If a user profile does exist.
    else:
        # user_posts = models.UserPosts.objects.filter(
        #     user_profile=user_profile).order_by('-created_at')

        request_profile = models.UserProfile.objects.get(user=request.user)

        # Annotating each post with info about whether the current user has liked it.
        user_posts = user_posts.annotate(
            user_has_liked=Exists(models.Like.objects.filter(
                user_profile=request_profile, post=OuterRef("pk")
            ))
        )

        is_following = request_profile.following.filter(
            id=user_profile.id).exists()

        if request.method == 'POST':
            post_id = request.POST.get("post-id")

            if 'comment-submit' in request.POST:
                comment_form = forms.CommentForm(request.POST)

                if comment_form.is_valid():
                    content = comment_form.cleaned_data['content']

                    post = get_object_or_404(
                        models.UserPosts,
                        id=int(post_id)
                    )

                    post.comment(user_profile=request_profile, content=content)
                    return redirect(reverse("community:user", args=[user_profile_id]))
                else:
                    return HttpResponseBadRequest("Invalid form data")

        if request_profile != user_profile:
            return render(
                request,
                "./community/user.html",
                {
                    "title": f"{user_profile.username}'s Profile",
                    "user_profile": user_profile,
                    "user_posts": user_posts,
                    "is_following": is_following,
                    "comment_form": comment_form,
                }
            )
        else:
            return redirect("community:profile")


@login_required
def profile_settings(request):
    """"""
    request_profile = models.UserProfile.objects.get(user=request.user)

    # Initialising a new form.
    profile_form = forms.UserPostsForm()

    if request.method == 'POST':
        profile_form = forms.UserProfileForm(request.POST,
                                    request.FILES,
                                    instance=request_profile)
        
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
            return redirect("community:profile-settings")
        else:
            return HttpResponseBadRequest("Invalid form data")

    return render(
        request,
        "./community/settings.html",
        {
            "title": f"{request_profile.username}'s settings",
            "profile_form": profile_form,
        }
    )


@login_required
def toggle_like(request, post_id):
    """"""
    # Getting the user profile of the request user.
    user_profile = get_object_or_404(models.UserProfile, user=request.user)
    # Getting the post object using the post id.
    post = get_object_or_404(models.UserPosts, id=post_id)

    liked = post.toggle_like(user_profile)

    # try:
    #     # Checking whether the user has already liked the post.
    #     like = models.Like.objects.get(user_profile=user_profile, post=post)

    #     # If the have liked the post before, the like will be deleted.
    #     like.delete()
    #     liked = False
    # except models.Like.DoesNotExist:
    #     # If the user hasn't liked the post before, a like will be added.
    #     models.Like.objects.create(user_profile=user_profile, post=post)
    #     liked = True

    # Returning the updated like count and whether the user has liked the post.
    like_count = post.get_like_count()
    response_data = {
        "like_count": like_count,
        "liked": liked
    }

    print("Response Data:", response_data)

    return JsonResponse(response_data)


@login_required
def toggle_follow(request, user_profile_id):
    """"""
    # Getting the user profile of the request user.
    request_profile = get_object_or_404(models.UserProfile, user=request.user)

    # Getting the user profile of the current page profile.
    user_profile = get_object_or_404(models.UserProfile, id=user_profile_id)

    # Toggling the follow status.
    is_following = request_profile.toggle_follow(user_profile)

    # Returning the updated followers and following count.
    followers_count = user_profile.get_followers_count()
    following_count = user_profile.get_following_count()

    response_data = {
        "followers_count": followers_count,
        "following_count": following_count,
        "is_following": is_following
    }

    print("Response Data:", response_data)

    return JsonResponse(response_data)


@login_required
def get_like_info(request, post_id):
    """"""
    # Getting the post.
    post = get_object_or_404(models.UserPosts, id=post_id)

    # Getting the like count for the post.
    like_count = post.likes.count()

    # Checking if the current user has liked the post.
    user_has_liked = models.Like.objects.filter(
        user_profile=request.user.userprofile, post=post).exists()

    # Preparing the JSON response.
    like_info = {
        'like_count': like_count,
        'user_has_liked': user_has_liked,
    }

    return JsonResponse(like_info)


# @login_required
# def post_comment(request, post_id):
#     if request.method == 'POST':
#         request_profile = models.UserProfile.objects.get(
#             user=request.user)

#         post = get_object_or_404(models.UserPosts, id=post_id)
#         # comment_form = forms.CommentForm(
#         #     user_profile=request_profile,
#         #     post=post_id,
#         #     text=request.POST.get("text")
#         # )

#         print(post)

#         # print(comment_form)

#         # if comment_form.is_valid():
#         #     text = comment_form.cleaned_data['text']
#         #     user_profile = models.UserProfile.objects.get(user=request.user)

#         #     post.comment(user_profile=user_profile, text=text)

#         #     # Return updated comments
#         #     comments = post.comments.all()
#         #     comments_data = [
#         #         {
#         #             'username': comment.user_profile.username,
#         #             'text': comment.text
#         #         } for comment in comments
#         #     ]

#         #     return JsonResponse(
#         #         {
#         #             'success': True,
#         #             'comments': comments_data
#         #         }
#         #     )

#     return JsonResponse(
#         {
#             'success': False
#         }
#     )
