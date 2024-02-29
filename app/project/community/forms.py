from django import forms
from .models import UserPosts, UserProfile


class UserPostsForm(forms.ModelForm):
    """
    Creates (adds) / updates a user post to the database.
    """

    class Meta:
        model = UserPosts
        fields = ['user_profile', 'post_picture', 'post_caption', 'created_at']
        widgets = {
            'user_profile': forms.HiddenInput(),
            'created_at': forms.HiddenInput(),
        }


class UserProfileForm(forms.ModelForm):
    """
    Creates a user profile for the user.
    """

    class Meta:
        model = UserProfile
        fields = ['user', 'username', 'profile_name', 'profile_picture', 'bio']

        widgets = {
            'user': forms.HiddenInput(),
        }
