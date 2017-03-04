from rest_framework.generics import (ListCreateAPIView, RetrieveDestroyAPIView)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from ..models.ads import Favourite
from ..serializers.ads import AdListSerializer
from ..serializers.user_favorites import UserFavoriteListSerializer

class UserFavoriteListView(ListCreateAPIView):
    serializer_class = UserFavoriteListSerializer

    def get_queryset(self):
        queryset = Favourite.objects.all()
        username = self.kwargs.get('username', None)
        queryset = queryset.filter(owner__username=username)
        return queryset

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
        fav_id = self.kwargs['pk']
        fav_queryset = Favourite.objects.filter(owner__username=username)
        try:
            return fav_queryset.get(id=fav_id)
        except Favourite.DoesNotExist:
            raise NotFound