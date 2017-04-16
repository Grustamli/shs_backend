from django.db.models.signals import (pre_save, post_save)
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from .models.user import (Profile, PrivacySetting)
from .models.search_alert import SearchAlert
from .models.contact import Contact
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
def autoGeneratePrivacySetting(sender, instance, created, *args, **kwargs):
    if created:
        PrivacySetting.objects.create(profile=instance)


@receiver(post_save, sender=Profile, weak=False, dispatch_uid="auto_create_contact_for_profile")
def autoCreateContactOnNewProfile(sender, instance, created, *args, **kwargs):
    if created:
        instance.contact.create()

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

@receiver(pre_save, sender=SearchAlert, weak=False, dispatch_uid='convert_to_lowercase')
def convertToLowerCase(sender, instance, *args, **kwargs):
    search_term = instance.search_term
    if instance.owner.search_alerts.filter(search_term=search_term.lower()).exists():
        raise ValidationError('search alert already exists')
    else:
        instance.search_term = search_term.lower()
