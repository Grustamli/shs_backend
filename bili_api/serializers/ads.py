from rest_framework import serializers
from .ad_extensions import (VehicleOnlyFieldsSerializer, PropertyOnlyFieldsSerializer)
from ..models.ads import Ad

class AdListSerializer(serializers.ModelSerializer):
    add_on_name = serializers.CharField(source='add_on.name')
    owner = serializers.CharField(source='owner.username', read_only=True)
    vehicle = VehicleOnlyFieldsSerializer()
    property = PropertyOnlyFieldsSerializer()
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        brief = self.context['request'].query_params.get('brief')
        if brief is not None and brief == 'true':
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(['uuid',])
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Ad
        fields = ('uuid', 'owner', 'title', 'price', 'description', 'add_on_name', 'vehicle', 'property')
        # extra_kwargs = {
        #     'owner':{
        #         'read_only': True,
        #     }
        # }

class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ('owner','uuid')

class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"
