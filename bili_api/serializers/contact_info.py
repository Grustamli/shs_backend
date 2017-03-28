from rest_framework import serializers
from ..models.contact_info import *
from ..models.ads import Ad
from ..models.user import Profile




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Address
        exclude     = ('id',)


class AddressOnlyContactSerializer(serializers.ModelSerializer):
    address         = AddressSerializer()
    class Meta:
        model       = ContactInfo
        fields      = ('address',)

class ContactInfoSerializer(serializers.ModelSerializer):
    address         = AddressSerializer()
    phone_number    = serializers.CharField(source='phone_number.number')
    website         = serializers.CharField(source='website.url')
    class Meta:
        model = ContactInfo
        fields = ('address','phone_number', 'website')
