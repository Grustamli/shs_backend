from rest_framework.generics import (ListCreateAPIView, RetrieveDestroyAPIView)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from ..models.ads import Favourite
from ..serializers.ads import AdListSerializer
from ..serializers.user_favorites import UserFavoriteListSerializer

class UserFavoriteListView(ListCreateAPIView):
    serializer_class = UserFavoriteListSerializer
    queryset = Favourite.objects.all()

    def list(self, request, username):
        queryset = self.get_queryset().filter(owner__username=username)
        serializer = UserFavoriteListSerializer(queryset, many=True)
        show_extended = request.query_params.get('extended', None)
        if show_extended is not None:
            ad_list = [item.ad for item in queryset]
            serializer = AdListSerializer(ad_list, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class UserFavoriteDetailView(RetrieveDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = UserFavoriteListSerializer
    def get_object(self):
        username = self.kwargs['username']
        ad = self.kwargs['ad_uuid']
        fav_queryset = Favourite.objects.filter(owner__username=username)
        try:
            return fav_queryset.get(ad=ad)
        except Favourite.DoesNotExist:
            raise NotFound
