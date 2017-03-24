from django.db import models

class PaymentPeriod(models.Model):
    name        = models.CharField(max_length=50, unique=True, primary_key=True)
    lang_az     = models.CharField(max_length=50, null=True, blank=True)
    lang_en     = models.CharField(max_length=50, null=True, blank=True)
    lang_ru     = models.CharField(max_length=50, null=True, blank=True)
    lang_tr     = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name
