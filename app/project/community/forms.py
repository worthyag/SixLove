from django import forms
from .models import UserPosts, UserProfile


class UserPostsForm(forms.ModelForm):
    """
    Creates (adds) / updates a user post to the database.
    """

    class Meta:
        model = UserPosts
        fields = ['post_picture', 'post_caption']


class UserProfileForm(forms.ModelForm):
    """
    Creates a user profile for the user.
    """

    class Meta:
        model = UserProfile
        fields = ['username', 'profile_name', 'profile_picture', 'bio']
