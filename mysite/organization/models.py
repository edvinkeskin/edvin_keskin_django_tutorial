from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.first_name


class Office(models.Model):
    number_of_employees = models.IntegerField(default=0)


class Organization(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    offices = models.ManyToManyField(Office)

    def __str__(self):
        return self.name


class Customer(models.Model):
    organizations = models.ManyToManyField(Organization)
