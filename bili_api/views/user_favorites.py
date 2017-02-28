from rest_framework.generics import (ListCreateAPIView, RetrieveDestroyAPIView)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from ..models.ads import Favourite
from ..serializers.ads import AdListSerializer
from ..serializers.user_favorites import UserFavoriteListSerializer
from ..models.user import Person


class UserFavoriteListView(ListCreateAPIView):
    serializer_class = UserFavoriteListSerializer

    def get_queryset(self):
        queryset = Favourite.objects.all()
        user_id = self.kwargs.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(person_id=user_id)
        return queryset

    def list(self, request, user_id):
        queryset = self.get_queryset()
        serializer = UserFavoriteListSerializer(queryset, many=True)
        show_extended = request.query_params.get('extended', None)
        if show_extended is not None:
            ad_list = [item.ad for item in queryset]
            serializer = AdListSerializer(ad_list, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):

        user = self.request.user
        person = Person.objects.get(id=user.id)
        serializer.save(person=person)


class UserFavoriteDetailView(RetrieveDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = UserFavoriteListSerializer
    def get_object(self):
        print(self.request)
        print(self.request.data)
        print(self.request.query_params)
        print(self.request.method)
        print(self.request.parsers)
        print(self.request.accepted_renderer)
        print(self.request.accepted_media_type)
        print(self.request.user)
        print(self.request.auth)
        print(self.request.content_type)
        print(self.request.stream)
        print(self.request.META)
        print(self.request.session)

        pk = self.kwargs['pk']
        user_id = self.kwargs['user_id']
        person = Person.objects.get(pk=user_id)
        fav_queryset = Favourite.objects.filter(person=person)
        fav_obj = None
        try:
            fav_obj = fav_queryset.get(id=pk)
        except Favourite.DoesNotExist:
            error = {"ad": "Requested object does not exist"}
            raise NotFound


        return fav_obj
