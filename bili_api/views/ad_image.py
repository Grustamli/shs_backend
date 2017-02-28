from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from ..models.ads import (Ad, AdImage)
from ..serializers.ad_image import (AdImageListSerializer,)


class AdImageListApiView(ListCreateAPIView):
    serializer_class = AdImageListSerializer
    def get_queryset(self, *args, **kwargs):
        queryset = AdImage.objects.all()
        ad_id = self.kwargs['ad_id']
        if ad_id is not None:
            queryset = queryset.filter(ad__id=ad_id)
        return queryset

    def perform_create(self, serializer):
        ad_id = self.kwargs['ad_id']
        ad = Ad.objects.get(pk=ad_id)
        serializer.save(ad=ad)

class AdImageDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdImageListSerializer
    queryset = AdImage.objects.all()
    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.instance
    #     print(instance)
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     return Response(serializer.data)
