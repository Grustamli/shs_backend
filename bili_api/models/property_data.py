from django.db import models

class PaymentPeriod(models.Model):
    name = models.CharField(max_length=50, unique=True)
    az = models.CharField(max_length=50, null=True, blank=True)
    en = models.CharField(max_length=50, null=True, blank=True)
    ru = models.CharField(max_length=50, null=True, blank=True)
    tr = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name
