from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from contact.models import Contact
from login.models import Login
from .forms import DeleteContactForm, EditContactForm, CreateContactForm, CreateMapForm
import requests
#from user.views import user_home

from django.http import HttpResponseRedirect
# Create your views here.

def createContact(request, id):
    if request.method=="POST":
        form = CreateContactForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                house_number = form.cleaned_data['house_number']
                street = form.cleaned_data['street']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                zipcode = form.cleaned_data['zipcode']
                phone_number = form.cleaned_data['phone_number']
                email = form.cleaned_data['email']
                workplace = form.cleaned_data['workplace']

                user1 = get_object_or_404(Login, pk=id)
                contacts = Contact.objects.filter(associated_user=id)

                c = Contact(fname=fname, lname=lname, house_number=house_number, street=street, city=city, state=state,zipcode=zipcode,phone_number=phone_number, email=email, workplace=workplace, associated_user=user1)
                c.save()

                return redirect('user_home', user1.id)
    else:
        form = CreateContactForm()
    return render(request, "contact/create_contact_form.html", {"form": form, "id":id})

def editContact(request, contactid):
    if request.method=="POST":
        form = EditContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            house_number = form.cleaned_data['house_number']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            workplace = form.cleaned_data['workplace']

            contacts = Contact.objects.filter(id=contactid)
            contact = contacts[0]

            c=get_object_or_404(Contact, pk=contact.id)
            c.house_number = house_number
            c.fname = fname
            c.lname = lname
            c.street = street
            c.city = city
            c.state = state
            c.zipcode = zipcode
            c.phone_number = phone_number
            c.email = email
            c.workplace = workplace

            c.save()

            associated_user_id = c.associated_user_id
            user1 = get_object_or_404(Login, pk=associated_user_id)

            return redirect('user_home', user1.id)
    else:
        contacts = Contact.objects.filter(id=contactid)
        contact = contacts[0]
        form = EditContactForm(initial={'fname':contact.fname,
                                        'lname':contact.lname,
                                        'house_number':contact.house_number,
                                        'street':contact.street,
                                        'city':contact.city,
                                        'state':contact.state,
                                        'zipcode':contact.zipcode,
                                        'phone_number':contact.phone_number,
                                        'email':contact.email,
                                        'workplace':contact.workplace
                                        })
    return render(request, "contact/edit_contact_form2.html", {"form": form, "contactid":contactid})


def deleteContact(request, contactid):
        instance = get_object_or_404(Contact, pk=contactid)
        associated_user_id = instance.associated_user_id
        instance.delete()

        user1 = get_object_or_404(Login, pk=associated_user_id)

        return redirect('user_home', user1.id)

def contactDetails(request, contactid):
    instance = get_object_or_404(Contact, pk=contactid)
    associated_user_id = instance.associated_user_id
    user1 = get_object_or_404(Login, pk=associated_user_id)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/



    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

    key = 'AIzaSyAkrYcTB0UQsgkxo2WHYUcztl4nPjE7VbA'

    params = {
        'address': str(instance.house_number)+' '+str(instance.street)+' '+str(instance.state)+' '+str(instance.zipcode),
        'sensor': 'false',
        'region': 'USA',
        'key': key
    }
    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    # Use the first result
    result = res['results'][0]

    lat = result['geometry']['location']['lat']
    long = result['geometry']['location']['lng']


    return render(request, "contact/contact_details.html", {"contact":instance, "user":user1, "lat":lat, "long": long})

def createMap(request, contactid):
    instance = get_object_or_404(Contact, pk=contactid)
    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

    key = 'AIzaSyAkrYcTB0UQsgkxo2WHYUcztl4nPjE7VbA'

    params = {
        'address': str(instance.house_number) + ' ' + str(instance.street) + ' ' + str(instance.state) + ' ' + str(
            instance.zipcode),
        'sensor': 'false',
        'region': 'USA',
        'key': key
    }
    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    # Use the first result
    result = res['results'][0]

    lat = result['geometry']['location']['lat']
    long = result['geometry']['location']['lng']

    return render(request, "contact/Map.html", {"lat":lat, "long":long, "contactid":contactid})
