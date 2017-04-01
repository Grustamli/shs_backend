from rest_framework.serializers import ModelSerializer
from ..models.ads import AdImage

class AdImageListSerializer(ModelSerializer):
    def create(self, validated_data, *args, **kwargs):
        print(validated_data)
        
    class Meta:
        model = AdImage
        fields = '__all__'
        extra_kwargs = {
            'ad':{
                'write_only' : True
            }
        }
