from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from .user import (
                Person,
                UserAddress,
                )
from .categories import Category
import datetime

class Ad(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='ads')
    category = models.ForeignKey(Category, related_name='ads')
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField()
    price = models.IntegerField(default=0)
    published = models.DateTimeField('publish date', auto_now_add=True)
    active_from = models.DateField(null=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
    def user_directory_path(instance, filename):
        ad_name = instance.ad.title
        return 'ads/{0}/{1}'.format(ad_name,filename)

    image = models.ImageField(upload_to=user_directory_path)
    def __str__(self):
        return self.ad.title

class Favourite(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='favourites')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('person', 'ad')



class Message(models.Model):
    sender = models.ForeignKey(Person, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Person, related_name='received_messages', on_delete=models.CASCADE)
    sent_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class AdAddress(models.Model):
    person = models.OneToOneField(Ad, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=150)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.address + ', ' + self.region + ', ' + self.city
