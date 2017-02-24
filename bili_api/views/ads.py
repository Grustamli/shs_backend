from ..serializers.ads import (AdListSerializer, AdCreateSerializer)
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from ..models.ads import Ad

class AdListView(ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AdCreateSerializer
        return super(AdListView, self).get_serializer_class()
