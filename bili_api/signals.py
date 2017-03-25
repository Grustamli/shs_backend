from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.user import Profile
from django.contrib.auth.models import User

# Auto Create Profile for each new user
@receiver(post_save, sender=User, dispatch_uid="create_profile_item")
def autoCreateProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


# Auto generate privacy setting for profile
@receiver(post_save, sender=Profile, dispatch_uid="create_privacy_settings_item")
def autoGeneratePrivacySetting(sender, instance, created, **kwargs):
    if created:
        PrivacySetting.objects.create(profile=instance)
