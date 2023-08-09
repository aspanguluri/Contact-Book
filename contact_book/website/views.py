from django.shortcuts import render
from login.models import Login

# Create your views here.

def home(request):
    return render(request, 'website/home.html',
                  {
                      "Logins":Login.objects.all()
                  })