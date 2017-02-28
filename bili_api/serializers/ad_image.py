from rest_framework.serializers import ModelSerializer
from ..models.ads import AdImage

class AdImageListSerializer(ModelSerializer):
    class Meta:
        model = AdImage
        fields = ('image',)
