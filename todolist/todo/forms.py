from django.forms import ModelForm
from django import forms

from . models import Todo

class TodoForm(ModelForm):

    title = forms.CharField(
        max_length=50,
        required= True
        
    )

    class Meta:
        model = Todo
        fields = ['title', 'description', ]

