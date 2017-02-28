from rest_framework.serializers import (ModelSerializer, CharField)
from ..models.ads import Favourite


class UserFavoriteListSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('id','ad',)
