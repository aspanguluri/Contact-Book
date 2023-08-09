from django.urls import path

from . import views

urlpatterns = [
    path('createLogin', views.createLogin, name = "createLogin"),
    path('signIn', views.signIn, name = "signIn"),
    path('deleteLogin/<int:loginid>', views.deleteLogin, name = 'deleteLogin'),
]