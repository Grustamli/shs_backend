from rest_framework.serializers import ModelSerializer
from ..models.ads import AdImage

class AdImageListSerializer(ModelSerializer):        
    class Meta:
        model = AdImage
        fields = '__all__'
        extra_kwargs = {
            'ad':{
                'write_only' : True
            }
        }
