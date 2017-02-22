from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator
from .ads import Ad
from .car_data import (CarBody, CarFuel, CarMake, CarTransmission)
from .property_data import PaymentPeriod
import datetime

# Creating models for categories
class Property(Ad):
    no_bed_room = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    payment = models.ForeignKey(PaymentPeriod)

    def __str__(self):
        return self.ad.title



class Vehicle(Ad):
    YEAR_CHOICES = []
    for r in range(1960, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    ad = models.OneToOneField(Ad, related_name='vehicle')
    make = models.ForeignKey(CarMake, null=True)
    body = models.ForeignKey(CarBody, null=True)
    fuel = models.ForeignKey(CarFuel, null=True)
    transmission = models.ForeignKey(CarTransmission, null=True)
    mileage = models.IntegerField(validators=[MaxValueValidator(9999999999)], null=True, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
    engine_size = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
