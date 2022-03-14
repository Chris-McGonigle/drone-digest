from django.forms import ModelForm
from .models import Thread


class ThreadForm(ModelForm):
    """
    Form to allow users to create a new thread
    """
    class Meta:
        model = Thread
        fields = ['subject', 'name', 'description']
        