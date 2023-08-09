from django.urls import path

from . import views

urlpatterns = [
    path('createContact/<int:id>', views.createContact, name = 'createContact'),
    path('editContact/<int:contactid>', views.editContact, name = 'editContact'),
    path('deleteContact/<int:contactid>', views.deleteContact, name = 'deleteContact'),
    path('contactDetails/<int:contactid>', views.contactDetails, name = 'contactDetails'),
    path('createMap/<int:contactid>', views.createMap, name = 'createMap'),
]