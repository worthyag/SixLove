from django import forms
from .models import TennisSession


class TennisSessionForm(forms.ModelForm):
    """
    Creates (adds) / updates a tennis session object / tennis session to the database.
    """
    class Meta:
        model = TennisSession
        fields = ['category', 'title', 'notes', 'date', 'is_completed']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
