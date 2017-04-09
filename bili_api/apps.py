from django.apps import AppConfig
from django.dispatch import receiver
from django.db.models.signals import post_save


class BiliApiConfig(AppConfig):
    name = 'bili_api'
    def ready(self):
        from .signals import (autoCreateProfile, autoGeneratePrivacySetting, \
        generateThumbnailForAd, convertToLowerCase)
