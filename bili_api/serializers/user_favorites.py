from rest_framework import serializers
from ..models.ads import (Favourite, Ad)


class UserFavoriteListSerializer(serializers.ModelSerializer):
    uuid = serializers.PrimaryKeyRelatedField(queryset=Ad.objects.all(), source='ad')
    class Meta:
        model = Favourite
        fields = ('uuid',)
