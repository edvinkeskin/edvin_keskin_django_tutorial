from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default="123 Road")
    city = models.CharField(max_length=200, default="Vancouver")
    province = models.CharField(max_length=200, default="BC")
    postal_code = models.CharField(max_length=200, default="V6T1Z1")
    country = models.CharField(max_length=200, default="Canada")
    phone_no = models.CharField(max_length=200, default="6045254590")

    def __str__(self):
        return self.user.username


class Office(models.Model):
    name = models.CharField(max_length=200, default="office a")
    address = models.CharField(max_length=200, default="123 Road")
    city = models.CharField(max_length=200, default="Vancouver")
    province = models.CharField(max_length=200, default="BC")
    postal_code = models.CharField(max_length=200, default="V6T1Z1")
    country = models.CharField(max_length=200, default="Canada")
    phone_no = models.CharField(max_length=200, default="6045254590")
    employees = models.ManyToManyField(Employee)


class Organization(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default="123 Road")
    city = models.CharField(max_length=200, default="Vancouver")
    province = models.CharField(max_length=200, default="BC")
    postal_code = models.CharField(max_length=200, default="V6T1Z1")
    country = models.CharField(max_length=200, default="Canada")
    phone_no = models.CharField(max_length=200, default="6045254590")
    offices = models.ManyToManyField(Office)

    def __str__(self):
        return self.name


class Customer(models.Model):
    organizations = models.ManyToManyField(Organization)
