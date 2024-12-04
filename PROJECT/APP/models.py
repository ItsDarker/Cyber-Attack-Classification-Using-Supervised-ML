from django.db import models
from django.contrib.auth.models import User


class UserPersonalModel(models.Model):


    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)   
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


def __str__(self):
    return self.firstname, self.lastname, self.age,self.address,self.phone,self.city,self.state,self.country