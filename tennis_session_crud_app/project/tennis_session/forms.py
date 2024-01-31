from django import forms
from .models import TennisSession


class AddTennisSessionForm(forms.ModelForm):
    """
    Creates a tennis session object / add a tennis session to the database.
    """
    # title = forms.CharField(max_length=150)
    # notes = forms.Textarea()
    # date = forms.DateTimeField()
    # is_completed = forms.BooleanField()

    class Meta:
        model = TennisSession
        fields = ['title', 'notes', 'date', 'is_completed']
