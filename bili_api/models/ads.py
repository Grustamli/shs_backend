from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from .contact import Contact
from django.db.models.signals import post_save
from os.path import splitext

from .geolocation import City
# from .user import (UserAddress,)
from .categories import Category
import datetime
from  base64 import urlsafe_b64encode
from uuid import uuid4


def post_image_directory_path(instance, filename):
    filename, file_extension = splitext(filename)
    ad = instance.ad.uuid
    return f'post-images/{ad}/{instance.pk}{file_extension}'

def thumbnails_directory_path(instance, filename):
    return f'post-thumbs/s300/{filename}'


class Ad(models.Model):
    uuid            = models.CharField(primary_key=True, editable=False, max_length=100)
    owner           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    category        = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='ads')
    title           = models.CharField(max_length=250)
    description     = models.TextField(null=True, blank=True)
    price           = models.IntegerField(null=True, blank=True)
    negotiable      = models.BooleanField(default=False)
    published       = models.DateTimeField('publish date', auto_now_add=True)
    active_from     = models.DateField(null=True, blank=True)
    contact         = GenericRelation(Contact)
    def save(self, *args, **kwargs):
        self.uuid = urlsafe_b64encode(uuid4().bytes).decode().rstrip("==")
        if not self.price:
            self.negotiable = True
        super().save(*args, **kwargs)
    def __str__(self):
        return self.uuid


class AdImage(models.Model):
    uuid            = models.CharField(primary_key=True, editable=False, max_length=100)
    ad              = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
    image           = models.ImageField(upload_to=post_image_directory_path)
    def save(self, *args, **kwargs):
        self.uuid = urlsafe_b64encode(uuid4().bytes).decode().rstrip("==")
        super().save(*args, **kwargs)
    def __str__(self):
        return self.uuid


class Thumbnail(models.Model):
    ad              = models.OneToOneField(Ad, on_delete=models.CASCADE, null=True, blank=True)
    image_s300      = models.ImageField(upload_to=thumbnails_directory_path)
    def save(self, *args, **kwargs):
        self.uuid = urlsafe_b64encode(uuid4().bytes).decode().rstrip("==")
        super().save(*args, **kwargs)
    def __str__(self):
        return self.ad.uuid



class Favourite(models.Model):
    owner           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    ad              = models.ForeignKey(Ad, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('owner', 'ad')


class Message(models.Model):
    sender          = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver        = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    sent_time       = models.DateTimeField(auto_now_add=True)
    content         = models.TextField()
