from django.db import models
from login.models import Login

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    house_number = models.IntegerField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.CharField(max_length=200)
    workplace = models.CharField(max_length=200)


    associated_user = models.ForeignKey(Login, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.fname} {self.lname}"