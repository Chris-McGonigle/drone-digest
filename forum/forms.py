from django.forms import ModelForm
from .models import Thread 

# Form to allow users to create a new thread 

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'