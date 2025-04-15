from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms  

from typing import List

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'style':'width:100%; box-sizing:border-box; padding:0.5em; border: 1px solid black;',
                'autocomplete': 'off'
            }
        )
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'width:100%; box-sizing:border-box; padding: 0.5em; border: 1px solid black;',
                'autocomplete': 'off'
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'width:100%; box-sizing:border-box; padding: 0.5em; border: 1px solid black;',
                'autocomplete': 'off' 
            }
        )
    )

    password2 = forms.CharField( 
        label='Confirm Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'width:100%; box-sizing:border-box; padding: 0.5em; border: 1px solid black;',
                'autocomplete': 'off' 
            }
        )
    )
    



    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:100%; box-sizing:border-box; padding: 0.5em; border: 1px solid black;',
                'autocomplete': 'off',
            }
        )
    )

    password = forms.CharField(
    max_length=50,
    widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
            'autocomplete':'off',
            'style':'width:100%; padding:0.5em; box-sizing: border-box; border: 1px solid black;'
        }
    )
    )

