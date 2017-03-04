from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify

# Create your models here.

class PhoneNumber(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='phone_number', blank=True, null=True)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    number = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    @property
    def person__username(self):
        return self.owner.username

    def __str__(self):
        return self.number

class UserAddress(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=150)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.address + ', ' + self.region + ', ' + self.city

class ProfilePic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_pic")
    def __str__(self):
        return self.owner.username


class PrivacySetting(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='privacy_setting')
    phone_visible = models.BooleanField(default=False)
    email_visible = models.BooleanField(default=False)
    address_visible = models.BooleanField(default=False)
