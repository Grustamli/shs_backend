from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .geolocation import City

class Address(models.Model):
    city            = models.ForeignKey(City, on_delete=models.PROTECT, related_name='addresses')
    def __str__(self):
        return self.city.name

class PhoneNumber(models.Model):
    number          = models.CharField(max_length=20)
    def __str__(self):
        return self.number

class Website(models.Model):
    url             = models.CharField(max_length=100)
    def __str__(self):
        return self.url


class Contact(models.Model):
    address         = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone_number    = models.OneToOneField(PhoneNumber, on_delete=models.CASCADE, null=True, blank=True)
    website         = models.OneToOneField(Website, on_delete=models.CASCADE, null=True, blank=True)

    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.CharField(max_length=50)
    content_object  = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('content_type', 'object_id')
