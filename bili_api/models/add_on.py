from django.db import models
from .ads import Ad
from datetime import timedelta



class AddOnType(models.Model):
    name            = models.CharField(primary_key=True, max_length=15)
    lang_az         = models.CharField(max_length=30, null=True, blank=True)
    lang_en         = models.CharField(max_length=30, null=True, blank=True)
    lang_ru         = models.CharField(max_length=30, null=True, blank=True)
    lang_tr         = models.CharField(max_length=30, null=True, blank=True)
    desc_az         = models.TextField(null=True, blank=True)
    desc_en         = models.TextField(null=True, blank=True)
    desc_tr         = models.TextField(null=True, blank=True)
    desc_ru         = models.TextField(null=True, blank=True)
    expiry_days     = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class AppliedAddOn(models.Model):
    ad              = models.OneToOneField(Ad, on_delete=models.CASCADE, related_name="add_on")
    add_on_type     = models.ForeignKey(AddOnType, on_delete=models.CASCADE)
    add_date        = models.DateTimeField('addon add date', auto_now_add=True)


    def __str__(self):
        return self.add_on_type.name
