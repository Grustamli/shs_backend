from rest_framework import serializers

from ..models.ads import Ad

class AdListSerializer(serializers.ModelSerializer):
    add_on_name = serializers.CharField(source='add_on.name')
    class Meta:
        model = Ad
        fields = ('id', 'person', 'title', 'price', 'description', 'add_on_name' )

class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ('slug',)


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ('slug','person')
