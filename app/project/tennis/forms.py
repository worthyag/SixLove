from django import forms
from django.contrib.auth import get_user_model
from .models import TennisSession


class TennisSessionForm(forms.ModelForm):
    """
    Creates (adds) / updates a tennis session object / tennis session to the database.
    """
    users = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = TennisSession
        fields = ['category', 'title', 'notes',
                  'date', 'is_completed', 'users']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(TennisSessionForm, self).__init__(*args, **kwargs)
        # Limit choices to users the current user is following
        self.fields['users'].queryset = user.userprofile.following.all()
