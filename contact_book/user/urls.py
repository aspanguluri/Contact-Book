from django.urls import path

from . import views

urlpatterns = [
    path('user_home/<int:id>', views.user_home, name='user_home'),
]