from django.db import models
from .ads import Ad
from datetime import timedelta



class AddOnType(models.Model):
    name = models.CharField(max_length=15)
    az = models.CharField(max_length=30, null=True, blank=True)
    en = models.CharField(max_length=30, null=True, blank=True)
    ru = models.CharField(max_length=30, null=True, blank=True)
    tr = models.CharField(max_length=30, null=True, blank=True)
    desc_az = models.TextField(null=True, blank=True)
    desc_en = models.TextField(null=True, blank=True)
    desc_tr = models.TextField(null=True, blank=True)
    desc_ru = models.TextField(null=True, blank=True)
    expiry_interval = models.IntegerField()



class AppliedAddOn(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="add_on")
    add_on = models.ForeignKey(AddOnType, on_delete=models.CASCADE, related_name="ads"),
    add_date = models.DateTimeField('addon add date', auto_now_add=True)

    def valid(self):
        ep = self.add_on.expiry_interval
        ep_sec = timedelta(days=ep).total_seconds()
        print(self.add_date)
