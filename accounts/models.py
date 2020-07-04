from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Customer(models.Model):
    """
    The customer model to create a
    new customer connected to an User
    A customer can only have 1 user & user only 1 customer
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    street_address = models.CharField(max_length=25)
    address_line_2 = models.CharField(max_length=25, blank=True, null=True)
    city = models.CharField(max_length=25)
    region = models.CharField(max_length=25, blank=True, null=True)
    postal = models.CharField(max_length=5)
    country = CountryField(multiple=False)
    email = models.CharField(max_length=25)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.company_name
