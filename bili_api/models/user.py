from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from .contact import Contact


class Profile(models.Model):
    owner           = models.OneToOneField(User, on_delete=models.CASCADE)
    contact         = GenericRelation(Contact)

    def profile_pic_directory_path(instance, filename):
        user = instance.owner.username
        return 'profile_pics/{0}/{1}'.format(user,filename)

    profile_pic     = models.ImageField(upload_to=profile_pic_directory_path, null=True)


    def __str__(self):
        return self.owner.username

class PrivacySetting(models.Model):
    profile         = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='privacy_setting')
    phone_visible   = models.BooleanField(default=False)
    email_visible   = models.BooleanField(default=False)
    address_visible = models.BooleanField(default=False)
