from django import forms
from .models import TennisSession


class AddTennisSessionForm(forms.ModelForm):
    """
    Creates a tennis session object / add a tennis session to the database.
    """
    class Meta:
        model = TennisSession
        fields = ['title', 'notes', 'date', 'is_completed']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
