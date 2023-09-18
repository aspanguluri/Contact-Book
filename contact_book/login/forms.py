from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField, PasswordInput
from django.core.exceptions import ValidationError
from django import forms

from .models import Login

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username', max_length=200)
    password = forms.CharField(label = 'password', widget=forms.PasswordInput)
    
