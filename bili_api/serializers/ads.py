from rest_framework import serializers
from .ad_extensions import (VehicleOnlyFieldsSerializer, PropertyOnlyFieldsSerializer)
from ..models.ads import Ad

class AdListSerializer(serializers.ModelSerializer):
    add_on              = serializers.CharField(source='add_on.name')
    owner               = serializers.CharField(source='owner.username', read_only=True)
    address             = serializers.StringRelatedField(read_only=True)
    phone_number        = serializers.StringRelatedField(read_only=True)
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

    class Meta:
        model = Ad
        fields = ('uuid', 'owner', 'title', 'price', 'description', 'address',
                    'phone_number', 'add_on', 'vehicle', 'property')


# TODO: Implement AdCreateSerializer
class AdCreateSerializer(serializers.ModelSerializer):
    city                = serializers.CharField(source='address.city')
    phone_number        = serializers.CharField(source='phone_number.phone_number')
    add_on              = serializers.CharField(source='add_on.name')
    class Meta:
        model = Ad
        fields = ('title', 'description', 'price', 'city', 'phone_number', 'add_on')

class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"
