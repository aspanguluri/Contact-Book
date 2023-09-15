from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField, PasswordInput
from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact

class DeleteContactForm(forms.Form):
    filler = forms.CharField(label = 'filler',widget=forms.HiddenInput, required = False)

class CreateContactForm(forms.Form):
    fname = forms.CharField(label='fname', max_length=200)
    lname = forms.CharField(label='lname', max_length=200)
    house_number = forms.IntegerField()
    street = forms.CharField(label='street', max_length=200)
    city = forms.CharField(label='city', max_length=200)
    state = forms.CharField(label='state', max_length=2)
    zipcode=forms.IntegerField()
    phone_number = forms.IntegerField()
    email = forms.CharField(label='email', max_length=200)
    workplace = forms.CharField(label='workplace', max_length=200)

class EditContactForm(forms.Form):
    fname = forms.CharField(label='fname', max_length=200)
    lname = forms.CharField(label='lname', max_length=200)
    house_number = forms.IntegerField()
    street = forms.CharField(label='street', max_length=200)
    city = forms.CharField(label='city', max_length=200)
    state = forms.CharField(label='state', max_length=2)
    zipcode = forms.IntegerField()
    phone_number = forms.IntegerField()
    email = forms.CharField(label='email', max_length=200)
    workplace = forms.CharField(label='workplace', max_length=200)

class CreateMapForm(forms.Form):
    lat = forms.CharField(label='lat')
    long = forms.CharField(label='long')
