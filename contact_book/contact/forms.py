from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField, PasswordInput
from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact

class DeleteContactForm(forms.Form):
    filler = forms.CharField(label = 'filler',widget=forms.HiddenInput, required = False)

# class EditContactForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         contactid = kwargs.pop('contactid')
#         super(EditContactForm, self).__init__(*args, **kwargs)
#         contacts = Contact.objects.filter(id=contactid)
#         contact = contacts[0]
#
#         self.fields['fname'].initial = contact.fname
#         self.fields['lname'].initial = contact.lname
#         self.fields['house_number'].initial = contact.house_number
#         self.fields['street'].initial = contact.street
#         self.fields['city'].initial = contact.city
#         self.fields['state'].initial = contact.state
#         self.fields['phone_number'].initial = contact.phone_number
#         self.fields['email'].initial = contact.email
#         self.fields['workplace'].initial = contact.workplace
#         self.fields['contact_id'].initial = contact.id
#
#     fname = forms.CharField(label='fname', max_length=200)
#     lname = forms.CharField(label='lname', max_length=200)
#     house_number = forms.IntegerField()
#     street = forms.CharField(label='street', max_length=200)
#     city = forms.CharField(label='city', max_length=200)
#     state = forms.CharField(label='state', max_length=2)
#     phone_number = forms.IntegerField()
#     email = forms.CharField(label='email', max_length=200)
#     workplace = forms.CharField(label='workplace', max_length=200)
#     contact_id=forms.IntegerField(widget=forms.HiddenInput(), required=False, label='contact_id')

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
    # def __init__(self, *args, **kwargs):
    #     contactid = kwargs.pop('contactid')
    #     super(EditContactForm, self).__init__(*args, **kwargs)
    #     contacts = Contact.objects.filter(id=contactid)
    #     contact = contacts[0]
    #
    #     self.fields['fname'].initial = contact.fname
    #     self.fields['lname'].initial = contact.lname
    #     self.fields['house_number'].initial = contact.house_number
    #     self.fields['street'].initial = contact.street
    #     self.fields['city'].initial = contact.city
    #     self.fields['state'].initial = contact.state
    #     self.fields['phone_number'].initial = contact.phone_number
    #     self.fields['email'].initial = contact.email
    #     self.fields['workplace'].initial = contact.workplace
    #     self.fields['contact_id'].initial = contact.id

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
    #contact_id=forms.IntegerField(widget=forms.HiddenInput(), required=False, label='contact_id')

class CreateMapForm(forms.Form):
    lat = forms.CharField(label='lat')
    long = forms.CharField(label='long')