from rest_framework import serializers
from ..models.user import *
from .contact_info import AddressRelatedField

class PrivacySettingListSerializer(serializers.ModelSerializer):
    class Meta:
        model           = PrivacySetting
        fields          = ('phone_visible', 'email_visible', 'address_visible')


class ProfileListSerializer(serializers.ModelSerializer):
    username            = serializers.CharField(source='owner.username')
    email               = serializers.CharField(source='owner.email')
    # address             = AddressRelatedField(read_only=True)
    phone_number        = serializers.StringRelatedField(many=True)
    class Meta:
        model           = Profile
        fields          = ('profile_pic','username', 'email','phone_number', 'privacy_setting')
