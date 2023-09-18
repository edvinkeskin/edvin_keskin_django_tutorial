from django.contrib.auth.models import User
from django.db import models


class AddressMixin(models.Model):
    address = models.CharField(max_length=200, default="123 Road")
    city = models.CharField(max_length=200, default="Vancouver")
    province = models.CharField(max_length=200, default="BC")
    postal_code = models.CharField(max_length=200, default="V6T1Z1")
    country = models.CharField(max_length=200, default="Canada")
    phone_no = models.CharField(max_length=200, default="6045254590")

    class Meta:
        abstract = True


class Employee(AddressMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Office(AddressMixin):
    name = models.CharField(max_length=200, default="office a")
    employees = models.ManyToManyField(Employee)


class Organization(AddressMixin):
    name = models.CharField(max_length=200)
    offices = models.ManyToManyField(Office)

    def __str__(self):
        return self.name


class Customer(models.Model):
    organizations = models.ManyToManyField(Organization)
