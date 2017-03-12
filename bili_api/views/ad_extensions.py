from rest_framework.generics import ListCreateAPIView
from ..serializers.ad_extensions import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models.ad_extensions import *

class VehicleAdListCreateView(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = VehicleAdListCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class PropertyAdListCreateView(ListCreateAPIView):
    queryset = Property.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = PropertyAdListCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
