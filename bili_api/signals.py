from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.user import (Profile, PrivacySetting)
from django.contrib.auth.models import User
from .models.ads import (AdImage, Thumbnail)
from PIL import Image
import os
from io import BytesIO
from django.core.files.base import ContentFile

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
        if not hasattr(instance.ad, 'thumbnail'):
            fname, fext = os.path.splitext(instance.image.name)
            filename = f'thumb_{instance.ad.uuid}{fext}'
            size = (300,300)
            img = Image.open(instance.image)
            img.thumbnail(size, Image.ANTIALIAS)
            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG')
            thumb_file = ContentFile(thumb_io.getvalue())

            thumbnail_obj = Thumbnail(ad=instance.ad)
            thumbnail_obj.image_s300.save(filename, thumb_file)
            thumbnail_obj.save()
            instance.ad.thumbnail = thumbnail_obj
            print(instance.ad.thumbnail)
