from rest_framework import serializers
from .ad_extensions import (VehicleOnlyFieldsSerializer, PropertyOnlyFieldsSerializer)
from ..models.ads import Ad
from ..models.ad_extensions import *
from ..models.contact_info import *
from ..models.add_on import *
from ..models.geolocation import City
from .contact_info import *
from .add_on import AppliedAddOnSerializer
from .ad_extensions import VehicleOnlyFieldsSerializer


class AdListSerializer(serializers.ModelSerializer):
    add_on              = serializers.CharField(source='add_on.add_on_type')
    contact_info        = AddressOnlyContactSerializer(many=True)
    vehicle             = VehicleOnlyFieldsSerializer()
    property            = PropertyOnlyFieldsSerializer()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brief = self.context['request'].query_params.get('brief')
        if brief is not None and brief == 'true':
            # Drop any fields that are not specified in the `fields` argument.
            allowed     = set(['uuid',])
            existing    = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def to_representation(self, obj):
        ret = super().to_representation(obj)
        vehicle_data    = ret.get('vehicle', None)
        property_data   = ret.get('property', None)
        add_on          = ret.get('add_on', None)
        if vehicle_data is None:
            ret.pop('vehicle')
        if property_data is None:
            ret.pop('property')
        if add_on is None:
            ret.pop('add_on')
        return ret

    class Meta:
        model = Ad
        fields = ('uuid', 'title', 'price','negotiable', 'description', 'contact_info',
                 'add_on', 'vehicle', 'property')

class AdCreateSerializer(serializers.ModelSerializer):
    contact_info            = ContactInfoSerializer(many=True)
    add_on                  = serializers.CharField(source='add_on.add_on_type')
    vehicle                 = VehicleOnlyFieldsSerializer(required=False)
    property                = PropertyOnlyFieldsSerializer(required=False)
    def create(self, validated_data):
        contact_data        = validated_data.pop('contact_info')
        add_on_data         = validated_data.pop('add_on')
        ad                  = None
        vehicle_data        = validated_data.get('vehicle', None)
        property_data       = validated_data.get('property', None)
        if vehicle_data is not None:
            vehicle_data    = validated_data.pop('vehicle')
            ad              = Vehicle.objects.create(**validated_data, **vehicle_data)
        elif property_data is not None:
            property_data   = validated_data.pop('property')
            ad              = Property.objects.create(**validated_data, **property_data)
        else:
            ad              = Ad.objects.create(**validated_data)

        print (ad)
        single_contact_info = contact_data[0]
        print (vehicle_data)
        if single_contact_info:
            address         = Address.objects.create(**single_contact_info['address'])
            phone_number    = PhoneNumber.objects.create(**single_contact_info['phone_number'])
            website         = Website.objects.create(**single_contact_info['website'])
            ad.contact_info.create(address=address, phone_number=phone_number, website=website)
        add_on_type         = AddOnType.objects.get(name=add_on_data['add_on_type'])
        AppliedAddOn.objects.create(ad=ad, add_on_type=add_on_type)
        return ad
    class Meta:
        model = Ad
        fields = ('title', 'description', 'category', 'price', 'negotiable', 'contact_info', 'add_on', 'vehicle', 'property')


# TODO: Implement AdUpdate
class AdDetailSerializer(serializers.ModelSerializer):
    contact_info            = ContactInfoSerializer(many=True)
    add_on                  = serializers.CharField(source='add_on.add_on_type')
    class Meta:
        model = Ad
        fields = ('title', 'description', 'category', 'price', 'negotiable', 'contact_info', 'add_on', 'images')
