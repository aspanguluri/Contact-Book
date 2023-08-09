from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField, PasswordInput
from django.core.exceptions import ValidationError
from django import forms

from .models import Login

class LoginForm(forms.Form):
    '''
    class Meta:
        model = Login
        fields = '__all__'
        widgets = {
            'username' : TextInput(attrs={"type":"text"}),
            'password' : PasswordInput(attrs={"type":"password"})
        }
    '''
    username = forms.CharField(label = 'username', max_length=200)
    password = forms.CharField(label = 'password', widget=forms.PasswordInput)

# class DeleteContactForm(forms.Form):
#