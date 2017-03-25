from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.user import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User, dispatch_uid="create_profile_item")
def autoCreateProfile(sender, instance, created, **kwargs):
    print('signal triggered')
    if created:
        Profile.objects.create(owner=instance)
