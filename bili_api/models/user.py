from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify

# Create your models here.

class Person(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.username


class PhoneNumber(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='phone_numbers', editable=False)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    number = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    @property
    def person__username(self):
        return self.person.username

    def __str__(self):
        return self.number

class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='addresses', editable=False)
    address = models.CharField(max_length=150)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


    def __str__(self):
        return self.address + ', ' + self.region + ', ' + self.city
