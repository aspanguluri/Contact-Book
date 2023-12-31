from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from login.models import Login
from contact.models import Contact
from .forms import LoginForm
from django.core.exceptions import ValidationError
from django.http import HttpResponse
# Create your views here.

createLoginForm = modelform_factory(Login, exclude=[])

def createLogin(request):
    if request.method=="POST":
        form = createLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            flag = False
            query = Login.objects.all()
            for i in query:
                if i.username==username:
                    flag = True
            if not flag:
                form.save()
                return redirect("home")
            else:
                form = createLoginForm()
    else:
        form = createLoginForm()
    return render(request, "login/create_login_form.html", {"form": form})


def signIn(request):

    if request.method=="POST":

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            query = Login.objects.filter(username = username)
            if len(query)>0:
                if query[0].password==password:
                    user1 = get_object_or_404(Login, pk = query[0].id)
                    contacts = Contact.objects.filter(associated_user=query[0])
                    return redirect('user_home', user1.id)
            else:
                form = LoginForm()
            return render(request, "login/sign_in_form.html", {"form": form})
    else:
        form=LoginForm()
        return render(request, "login/sign_in_form.html", {"form":form})

def deleteLogin(request, loginid):
    login = get_object_or_404(Login, pk=loginid)

    contacts = Contact.objects.filter(associated_user=login)

    for i in range(0,len(contacts)):
        instance = contacts[i]
        instance.delete()

    login.delete()

    return redirect('home')
