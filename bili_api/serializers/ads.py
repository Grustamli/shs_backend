from rest_framework import serializers

from ..models.ads import Ad

class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'title', 'price', 'description')

class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
