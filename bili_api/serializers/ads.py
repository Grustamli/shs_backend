from rest_framework import serializers

from ..models.ads import Ad

class AdListSerializer(serializers.ModelSerializer):
    add_on_name = serializers.CharField(source='add_on.name')
    owner = serializers.CharField(source='owner.username')
    class Meta:
        model = Ad
        fields = ('uuid', 'owner', 'title', 'price', 'description', 'add_on_name' )

class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ('owner','uuid')

class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"
