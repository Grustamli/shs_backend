from rest_framework.generics import (ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView)
from rest_framework.response import Response
from rest_framework.parsers import (MultiPartParser, JSONParser, FormParser)
from ..models.ads import (Ad, AdImage)
from ..serializers.ad_image import (AdImageListSerializer,)



# class AdImageListAPIView(ListAPIView):
#     serializer_class = AdImageListSerializer
#     def get_queryset(self, *args, **kwargs):
#         queryset = AdImage.objects.all()
#         ad_id = self.kwargs['ad_uuid']
#         if ad_id is not None:
#             queryset = queryset.filter(ad__uuid=ad_id)
#         return queryset

class AdImageListCreateAPIView(ListCreateAPIView):
    parser_classes = (FormParser,MultiPartParser)
    serializer_class = AdImageListSerializer
    queryset = AdImage.objects.all()
    # def create(self, request, *args, **kwargs):
    #     print(request.data)

class AdImageDetailApiView(RetrieveDestroyAPIView):
    serializer_class = AdImageListSerializer
    queryset = AdImage.objects.all()
