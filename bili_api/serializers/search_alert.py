from rest_framework.serializers import ModelSerializer
from ..models.search_alert import SearchAlert

class SearchAlertListSerializer(ModelSerializer):
    class Meta:
        model = SearchAlert
        exclude = ('owner',)

class SearchAlertDetailSerializer(ModelSerializer):
    class Meta:
        model = SearchAlert
        fields = ('notify',)
