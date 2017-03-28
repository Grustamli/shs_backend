from rest_framework import serializers
from ..models.contact import *
from ..models.ads import Ad
from ..models.user import Profile




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Address
        exclude     = ('id',)


class AddressOnlyContactSerializer(serializers.ModelSerializer):
    address         = AddressSerializer()
    class Meta:
        model       = Contact
        fields      = ('address',)

class ContactSerializer(serializers.ModelSerializer):
    address         = AddressSerializer()
    phone_number    = serializers.CharField(source='phone_number.number', required=False)
    website         = serializers.CharField(source='website.url', required=False)
    class Meta:
        model = Contact
        fields = ('address','phone_number', 'website')
