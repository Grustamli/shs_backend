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
    first_name          = serializers.CharField(source='owner.first_name')
    last_name           = serializers.CharField(source='owner.last_name')
    address             = serializers.StringRelatedField(read_only=True)
    phone_number        = serializers.StringRelatedField(read_only=True)
    website             = serializers.StringRelatedField(read_only=True)
    privacy_setting     = PrivacySettingListSerializer()
    class Meta:
        model           = Profile
        fields          = ('profile_pic','username', 'email', 'first_name', 'last_name',
                            'phone_number', 'address', 'website', 'privacy_setting')


# TODO: Implement Updating Profile
class ProfileUpdateSerializer(serializers.ModelSerializer):
    username            = serializers.CharField(source='owner.username')
    email               = serializers.CharField(source='owner.email')
    first_name          = serializers.CharField(source='owner.first_name')
    last_name           = serializers.CharField(source='owner.last_name')
    city                = serializers.CharField(source='address.city')
    phone_number        = serializers.StringRelatedField(read_only=True)
    website             = serializers.StringRelatedField(read_only=True)

    # def create()
    class Meta:
        model           = Profile
