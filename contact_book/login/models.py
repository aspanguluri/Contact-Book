from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    house_number = models.IntegerField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.username}"