from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    az = models.CharField(max_length=40, blank=True, null=True)
    en = models.CharField(max_length=40, blank=True, null=True)
    ru = models.CharField(max_length=40, blank=True, null=True)
    tr = models.CharField(max_length=40, blank=True, null=True)
    parent = models.ForeignKey('self', related_name="subcategories", blank=True, null=True)

    def __str__(self):
        return self.name
