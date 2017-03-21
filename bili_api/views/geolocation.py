from rest_framework.generics import ListAPIView
from ..serializers.geolocation import CityListSerializer
from ..models.geolocation import City

class CityListView(ListAPIView):
    serializer_class=CityListSerializer
    queryset=City.objects.all()
