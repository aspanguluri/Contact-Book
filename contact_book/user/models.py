from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    address = models.CharField(max_length=400)