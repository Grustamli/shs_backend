from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.user import (Profile, PrivacySetting)
from django.contrib.auth.models import User
from .models.ads import AdImage
from PIL import Image

# Auto Create Profile for each new user
@receiver(post_save, sender=User, weak=False, dispatch_uid="create_profile_item")
def autoCreateProfile(sender, instance, created, **kwargs):
    if created:
        if not Profile.objects.filter(owner = instance).exists():
            Profile.objects.create(owner=instance)


# Auto generate privacy setting for profile
@receiver(post_save, sender=Profile, weak=False, dispatch_uid="create_privacy_settings_item")
def autoGeneratePrivacySetting(sender, instance, created, **kwargs):
    if created:
        PrivacySetting.objects.create(profile=instance)


@receiver(post_save, sender=AdImage, weak=False, dispatch_uid="create_privacy_settings_item")
def generateThumbnailForAd(sender, instance, created, **kwargs):
    if created:
        if not instance.ad.thumbnail.exists():
            size = (300,300)
            img = Image.open(instance.image)
            instance.ad.thumbnail = img.thumbnail(size, Image.ANTIALIAS)
