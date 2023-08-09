from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from user.models import User
from contact.models import Contact
from login.models import Login
# Create your views here.
def user_home(request, id):
    user1 = get_object_or_404(Login, pk=id)
    contacts = Contact.objects.filter(associated_user=id)

    return render(request, "user/user_home.html", {"user":user1, "contacts":contacts})