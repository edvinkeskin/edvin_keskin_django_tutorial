from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    # You can add other fields here as needed

    def __str__(self):
        return self.first_name


class Office(models.Model):
    number_of_employees = models.IntegerField(default=0)


class Organization(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    offices = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE)
