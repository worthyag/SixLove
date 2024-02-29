from django import forms
from .models import UserPosts


class UserPostsForm(forms.ModelForm):
    """
    Creates (adds) / updates a user post to the database.
    """

    class Meta:
        model = UserPosts
        fields = ['post_picture', 'post_caption']
