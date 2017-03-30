from rest_framework import serializers
from ..models.ad_extensions import (Vehicle, Property)
from .contact import *

class VehicleAdListCreateSerializer(serializers.ModelSerializer):
    add_on              = serializers.CharField(source='add_on.add_on_type')
    contact        = AddressOnlyContactSerializer(many=True)
    class Meta:
        model = Vehicle
        fields = ('title', 'description', 'category', 'price', 'negotiable', 'contact', 'add_on',
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
