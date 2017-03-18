from rest_framework import serializers
from ..models.categories import Category
import re

class CategoryListSerializer(serializers.ModelSerializer):
    has_child = serializers.SerializerMethodField()
    def get_has_child(self, obj):
        print(obj.subcategories)
        return obj.subcategories.exists()
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        lang = self.context['request'].query_params.get('lang')
        if lang:
            lang = 'lang_'+lang
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(['name', lang, 'has_child'])
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Category
        fields = '__all__'
