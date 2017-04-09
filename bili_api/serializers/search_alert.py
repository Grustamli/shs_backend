from rest_framework.serializers import ModelSerializer
from ..models.search_alert import SearchAlert

class SearchAlertListSerializer(ModelSerializer):
    class Meta:
        model = SearchAlert
        exclude = ('notify', 'owner')
