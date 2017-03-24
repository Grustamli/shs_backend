from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from .geolocation import City

# Create your models here.

class ProfilePic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_pic")
    def __str__(self):
        return self.owner.username


class PrivacySetting(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='privacy_setting')
    phone_visible = models.BooleanField(default=False)
    email_visible = models.BooleanField(default=False)
    address_visible = models.BooleanField(default=False)
