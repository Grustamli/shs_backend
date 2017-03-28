from rest_framework import serializers
from ..models.ad_extensions import (Vehicle, Property)
from .contact_info import *

class VehicleAdListCreateSerializer(serializers.ModelSerializer):
    add_on              = serializers.CharField(source='add_on.add_on_type')
    contact_info        = AddressOnlyContactSerializer(many=True)
    def create(self, validated_data):
        contact_data        = validated_data.pop('contact_info')
        add_on_data         = validated_data.pop('add_on')
        ad                  = Ad.objects.create(**validated_data)
        single_contact_info = contact_data[0]
        if single_contact_info:
            address         = Address.objects.create(**single_contact_info['address'])
            phone_number    = PhoneNumber.objects.create(**single_contact_info['phone_number'])
            website         = Website.objects.create(**single_contact_info['website'])
            ad.contact_info.create(address=address, phone_number=phone_number, website=website)
        add_on_type         = AddOnType.objects.get(name=add_on_data['add_on_type'])
        AppliedAddOn.objects.create(ad=ad, add_on_type=add_on_type)
        return ad
    class Meta:
        model = Vehicle
        fields = ('title', 'description', 'category', 'price', 'negotiable', 'contact_info', 'add_on',
                'make', 'fuel', 'transmission', 'mileage', 'year', 'engine_size'
            )



class VehicleOnlyFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('make', 'body', 'fuel', 'transmission', 'mileage', 'year', 'engine_size')


class PropertyOnlyFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('no_bed_room', 'payment', 'area')

class PropertyAdListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        extra_kwargs = {
            'owner': {
                'read_only': True
            }
        }
