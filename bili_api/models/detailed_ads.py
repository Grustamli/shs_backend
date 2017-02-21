from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator
from .ads import Ad
import datetime

# Creating models for categories
class Property(models.Model):
    TYPE_CHOICES=(
        ('OFFICE', 'Office place'),
        ('HOME', (
            ('FlAT', 'Flat'),
            ('HOUSE', 'House'),
            )
        ),
        ('LAND', 'Land'),
        ('COMMERCIAL', 'Commercial'),
        ('UNKNOWN', 'Unknown')
    )
    STATUS_CHOICES=(
        ('RENT', 'Rent'),
        ('SALE', 'Sale'),
        ('SHARE', 'Share')
    )
    PAYMENT_CHOICES=(
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY','Monthly')
    )
    ad = models.OneToOneField(Ad,related_name='property')
    kind = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    no_bed_room = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    payment = models.CharField(max_length=7, choices=PAYMENT_CHOICES, default=PAYMENT_CHOICES[2][1])

    @property
    def ad__slug(self):
        return self.ad.slug

    def __str__(self):
        return self.ad.title

class Vehicle(models.Model):
    MAKE_CHOICES = (
        ('ANY', 'Any'),
        ('AC', 'AC'),
        ('ABARTH', 'Abarth'),
        ('AIXAM', 'Aixam'),
        ('ALFA_ROMEO', 'Alfa Romeo'),
        ('ASTON_MARTIN', 'Aston Martin'),
        ('AUDI', 'Audi'),
        ('AUSTIN', 'Austin'),
        ('BMW', 'BMW'),
        ('BENTLEY', 'Bentley'),
        ('BRISTOL', 'Bristol'),
        ('CADILLAC', 'Cadillac'),
        ('CATERHAM', 'Caterham'),
        ('CHEVROLET', 'Chevrolet'),
        ('CHERRY', 'Cherry'),
        ('CHRYSLER', 'Chrysler'),
        ('CITROEN', 'Citroen'),
        ('CORVETTE', 'Corvette'),
        ('DS', 'DS'),
        ('DACIA', 'Dacia'),
        ('DAEWOO', 'Daewoo'),
        ('DAIHATSU', 'Daihatsu'),
        ('DAIMLER', 'Daimler'),
        ('DODGE', 'Dodge'),
        ('FERRARI', 'Ferrari'),
        ('FIAT', 'Fiat'),
        ('FORD', 'Ford'),
        ('HONDA', 'Honda'),
        ('HUMMER', 'Hummer'),
        ('HYUNDAI', 'Hyundai'),
        ('INFINITI', 'Infiniti'),
        ('INVICTA', 'Invicta'),
        ('ISUZU', 'Isuzu'),
        ('JAGUAR', 'Jaguar'),
        ('JEEP', 'Jeep'),
        ('KTM', 'KTM'),
        ('KIA', 'KIA'),
        ('LTI', 'LTI'),
        ('LADA', 'Lada'),
        ('LAMBORGHINI', 'Lamborghini'),
        ('LANCIA', 'Lancia'),
        ('LAND_ROWER', 'Land Rower'),
        ('LEXUS', 'Lexus'),
        ('LOTUS', 'Lotus'),
        ('MG', 'MG'),
        ('MG_MOTOR_UK', 'MG Motor UK'),
        ('MASERATI', 'MASERATI'),
        ('MAZDA', 'Mazda'),
        ('MCLAREN', 'Mclaren'),
        ('MERCEDES_BENZ', 'Mercedes Benz'),
        ('MICROCAR', 'Microcar'),
        ('MINI', 'Mini'),
        ('MITSUBISHI', 'Mitsubishi'),
        ('MORGAN', 'Morgan'),
        ('NISSAN', 'Nissan'),
        ('OPEL', 'Opel'),
        ('PERODUA', 'Perodua'),
        ('PEUGEOT', 'Peugeot'),
        ('PORCHE', 'Porche'),
        ('PROTON', 'Proton'),
        ('RELIANT', 'Reliant'),
        ('RENAULT', 'Renault'),
        ('ROLLS_ROYCE', 'Rolls-Royce'),
        ('ROVER',' Rover'),
        ('SAAB', 'Saab'),
        ('SEAT', 'Seat'),
        ('SKODA', 'Skoda'),
        ('SMART', 'Smart'),
        ('SSANGYONG', 'Ssangyong'),
        ('SUBARU', 'Subaru'),
        ('SUZUKI', 'Suzuki'),
        ('TVR', 'TVR'),
        ('TALBOT', 'Talbot'),
        ('TATA', 'Tata'),
        ('TESLA', 'Tesla'),
        ('TOYOTA', 'Toyota'),
        ('VAUXHALL', 'Vauxhall'),
        ('VOLKSWAGEN', 'Volxwagen'),
        ('VOLVO', 'Volvo'),
        ('WESTFIELD', 'Westfield'),
        ('OTHER', 'Other')
    )

    BODY_CHOICES = (
        ('ANY', 'Any'),
        ('CAR_DERIVED_VAN', 'Car Derived Van'),
        ('CONVERTIBLE', 'Convertible'),
        ('COUPE', 'Coupe'),
        ('ESTATE', 'Estate'),
        ('HATCHBACK', 'Hatchback'),
        ('LIGHT4X4', 'Light 4x4'),
        ('MUSCLE', 'Muscle'),
        ('MINIBUS', 'Minibus'),
        ('MOTOR_CARAVAN', 'Motor Caravan'),
        ('MPV', 'MPV'),
        ('PANEL_VAN', 'Panel Van'),
        ('PICKUP', 'Pick Up'),
        ('SALOON', 'Saloon'),
        ('SPORTS', 'Sports'),
        ('WINDOW_VAN', 'Window Van'),
        ('OTHER', 'Other')
    )

    FUEL_CHOICES = (
        ('ANY', 'Any'),
        ('PETROL', 'Petrol'),
        ('DIESEL', 'Diesel'),
        ('GAS', 'Gas'),
        ('ELECTRIC', 'Electric'),
        ('GAS_BI_FUEL', 'Gas Bi Fuel'),
        ('HYBRID_ELECTRIC', 'Hybrid Electric'),
        ('PETROL/GAS', 'Petrol/Gas'),
        ('OTHER', 'Other')
    )

    TRANSMISSION_CHOICES = (
        ('ANY', 'Any'),
        ('AUTOMATIC', 'Automatic'),
        ('MANUAL', 'Manual'),
        ('SEMI-AUTO', 'Semi Auto'),
        ('OTHER', 'Other')
    )

    YEAR_CHOICES = []
    for r in range(1960, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    ad = models.OneToOneField(Ad, related_name='vehicle')
    make = models.CharField(max_length=20, choices=MAKE_CHOICES, null=True, blank='True', default=MAKE_CHOICES[0][1])
    mileage = models.IntegerField(validators=[MaxValueValidator(9999999999)], null=True, blank=True)
    body = models.CharField(max_length=15, choices=BODY_CHOICES, null=True, blank=True, default=BODY_CHOICES[0][1])
    fuel = models.CharField(max_length=15, choices=FUEL_CHOICES, null=True, blank=True, default=FUEL_CHOICES[0][1])
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, null=True, blank=True, default=TRANSMISSION_CHOICES[0][1])
    year = models.IntegerField(choices=YEAR_CHOICES,
                                default=datetime.datetime.now().year, null=True, blank=True)
    engine_size = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
