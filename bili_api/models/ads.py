from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from .contact_info import *
from django.db.models.signals import post_save

from .geolocation import City
# from .user import (UserAddress,)
from .categories import Category
import datetime
from  base64 import urlsafe_b64encode
from uuid import uuid4

class Ad(models.Model):
    uuid = models.CharField(primary_key=True, editable=False, max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='ads')
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    published = models.DateTimeField('publish date', auto_now_add=True)
    active_from = models.DateField(null=True, blank=True)
    address = GenericRelation(Address)
    phone_number = GenericRelation(PhoneNumber)
    def save(self, *args, **kwargs):
        self.uuid = urlsafe_b64encode(uuid4().bytes).decode().rstrip("==")
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title




class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
    def user_directory_path(instance, filename):
        ad = instance.ad.uuid
        return 'ad-images/{0}/{1}'.format(ad,filename)

    image = models.ImageField(upload_to=user_directory_path)
    def __str__(self):
        return self.ad.title

class Favourite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('owner', 'ad')



class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    sent_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()








# @receiver(post_save, sender=Ad)
# def my_callback(sender, instance, *args, **kwargs):
#     instance.uuid = instance.uuid.strip("=")
#     print(instance.id)
