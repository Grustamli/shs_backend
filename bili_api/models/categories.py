from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    lang_az = models.CharField(max_length=40, blank=True, null=True)
    lang_en = models.CharField(max_length=40, blank=True, null=True)
    lang_ru = models.CharField(max_length=40, blank=True, null=True)
    lang_tr = models.CharField(max_length=40, blank=True, null=True)
    parent = models.ForeignKey('self', related_name="subcategories", blank=True, null=True)

    def __str__(self):
        return self.name
