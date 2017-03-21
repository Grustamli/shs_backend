from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    lang_az = models.CharField(max_length=50)
    lang_en = models.CharField(max_length=50)
    lang_ru = models.CharField(max_length=50)
    lang_tr = models.CharField(max_length=50)
