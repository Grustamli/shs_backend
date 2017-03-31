from rest_framework import serializers
from .ad_extensions import (VehicleOnlyFieldsSerializer, PropertyOnlyFieldsSerializer)
from ..models.ads import Ad
from ..models.ad_extensions import *
from ..models.contact import *
from ..models.add_on import *
from ..models.geolocation import City
from .contact import *
from .add_on import AppliedAddOnSerializer
from .ad_extensions import VehicleOnlyFieldsSerializer
from .ad_image import AdImageListSerializer

class AdListSerializer(serializers.ModelSerializer):
    add_on              = serializers.CharField(source='add_on.add_on_type')
    contact             = AddressOnlyContactSerializer(many=True)
    vehicle             = VehicleOnlyFieldsSerializer()
    property            = PropertyOnlyFieldsSerializer()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brief = self.context['request'].query_params.get('brief')
        if brief is not None and brief == 'true':
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
        fields = ('uuid', 'category', 'title', 'price','negotiable', 'description', 'contact',
                 'add_on', 'vehicle', 'property')

class AdCreateSerializer(serializers.ModelSerializer):
    contact            = ContactSerializer(many=True, write_only=True)
    add_on                  = serializers.CharField(source='add_on.add_on_type', required=False, write_only=True)
    vehicle                 = VehicleOnlyFieldsSerializer(required=False, write_only=True)
    property                = PropertyOnlyFieldsSerializer(required=False, write_only=True)
    def create(self, validated_data):
        print(validated_data)
        contact_data        = validated_data.pop('contact')
        single_contact = contact_data[0]
        ad                  = None
        vehicle_data        = validated_data.get('vehicle', None)
        property_data       = validated_data.get('property', None)
        add_on_data         = validated_data.get('add_on', None)
        add_on_type         = None
        if add_on_data is not None:
            add_on_type     = AddOnType.objects.get(name=add_on_data['add_on_type'])
            validated_data.pop('add_on')

        if vehicle_data is not None:
            vehicle_data    = validated_data.pop('vehicle')
            vehicle_ad              = Vehicle.objects.create(**validated_data, **vehicle_data)
            ad              = Ad.objects.get(uuid=vehicle_ad.uuid)
        elif property_data is not None:
            property_data   = validated_data.pop('property')
            property_ad              = Property.objects.create(**validated_data, **property_data)
            ad              = Ad.objects.get(uuid=property_ad.uuid)
        else:
            ad              = Ad.objects.create(**validated_data)
        if single_contact is not None:
            address         = Address.objects.create(**single_contact['address']) if \
                single_contact.get('address') is not None else None
            phone_number    = PhoneNumber.objects.create(**single_contact['phone_number']) if \
                single_contact.get('phone_number') is not None else None
            website         = Website.objects.create(**single_contact['website']) if \
                single_contact.get('website') is not None else None
            ad.contact.create(address=address, phone_number=phone_number, website=website)
        if add_on_type is not None:
            AppliedAddOn.objects.create(ad=ad, add_on_type=add_on_type)
        return ad
    class Meta:
        model = Ad
        fields = ('uuid','title', 'description', 'category', 'price', 'negotiable', 'contact', 'add_on', 'vehicle', 'property')


# TODO: Implement AdUpdate
class AdDetailSerializer(serializers.ModelSerializer):
    contact             = ContactSerializer(many=True)
    add_on              = serializers.CharField(source='add_on.add_on_type', required=False)
    vehicle             = VehicleOnlyFieldsSerializer()
    property            = PropertyOnlyFieldsSerializer()
    images              = AdImageListSerializer(many=True)
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
        fields = ('title', 'description', 'category', 'price', 'negotiable',
            'contact', 'add_on', 'images', 'vehicle', 'property')
