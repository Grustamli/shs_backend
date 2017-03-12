from rest_framework.serializers import ModelSerializer
from ..models.ad_extensions import (Vehicle, Property)

class VehicleAdListCreateSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        extra_kwargs = {
            'owner': {
                'read_only': True
            }
        }


class VehicleOnlyFieldsSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('make', 'body', 'fuel', 'transmission', 'mileage', 'year', 'engine_size')


class PropertyOnlyFieldsSerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = ('no_bed_room', 'payment', 'area')

class PropertyAdListCreateSerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        extra_kwargs = {
            'owner': {
                'read_only': True
            }
        }
