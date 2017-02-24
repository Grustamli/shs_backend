from rest_framework.serializers import ModelSerializer
from ..models.vehicle_data import *


################################################################################

class VehicleBodyListSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        lang = self.context['request'].query_params.get('lang')
        print(lang)
        if lang:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(['name', lang])
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = VehicleBody
        fields = '__all__'

################################################################################

class VehicleFuelListSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        lang = self.context['request'].query_params.get('lang')
        print(lang)
        if lang:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(['name', lang])
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = VehicleFuel
        fields = '__all__'

################################################################################

class VehicleTransmissionListSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        lang = self.context['request'].query_params.get('lang')
        print(lang)
        if lang:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(['name', lang])
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = VehicleTransmission
        fields = '__all__'

################################################################################

class VehicleMakeListSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        lang = self.context['request'].query_params.get('lang')
        print(lang)
        if lang:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(['name', lang])
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = VehicleMake
        fields = '__all__'

################################################################################

class VehicleModelListSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        lang = self.context['request'].query_params.get('lang')
        print(lang)
        if lang:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(['name', lang])
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = VehicleModel
        fields = '__all__'
