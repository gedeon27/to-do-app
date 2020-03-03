from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    # task = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = ThingToDo
        fields = ['thing', 'completed']
