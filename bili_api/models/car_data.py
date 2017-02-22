from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=50, unique=True)
    az = models.CharField(max_length=50, null = True, blank = True)
    en = models.CharField(max_length=50, null = True, blank = True)
    ru = models.CharField(max_length=50, null = True, blank = True)
    tr = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    az = models.CharField(max_length=50, null = True, blank = True)
    en = models.CharField(max_length=50, null = True, blank = True)
    ru = models.CharField(max_length=50, null = True, blank = True)
    tr = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.name

class CarBody(models.Model):
    name = models.CharField(max_length=50, unique=True)
    az = models.CharField(max_length=50, null = True, blank = True)
    en = models.CharField(max_length=50, null = True, blank = True)
    ru = models.CharField(max_length=50, null = True, blank = True)
    tr = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.name

class CarTransmission(models.Model):
    name = models.CharField(max_length=50, unique=True)
    az = models.CharField(max_length=50, null = True, blank = True)
    en = models.CharField(max_length=50, null = True, blank = True)
    ru = models.CharField(max_length=50, null = True, blank = True)
    tr = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.name

class CarFuel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    az = models.CharField(max_length=50, null = True, blank = True)
    en = models.CharField(max_length=50, null = True, blank = True)
    ru = models.CharField(max_length=50, null = True, blank = True)
    tr = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.name
