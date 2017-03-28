from rest_framework.serializers import ModelSerializer
from ..models.add_on import *

class AddOnListSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lang = self.context['request'].query_params.get('lang')
        if lang:
            allowed = set(['name', lang, 'desc_'+lang])
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = AddOnType
        fields = "__all__"


class AppliedAddOnSerializer(ModelSerializer):
    class Meta:
        model = AppliedAddOn
        fields = '__all__'
