from ..serializers.ads import (AdListSerializer, AdCreateSerializer, AdDetailSerializer)
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from ..permissions import *
from django.http import Http404
from ..filters import AdFilter

from ..models.ads import Ad
from ..models.add_on import AppliedAddOn
from rest_framework.parsers import JSONParser


class AdListView(ListCreateAPIView):
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_class = AdFilter
    search_fields = ['$title', '$description']
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True, context={'request':request})
        return Response(serializer.data)


    def get_queryset(self):
        queryset = Ad.objects.all()
        username = self.request.query_params.get('user', None)
        if username is not None:
            user = User.objects.get(username=username)
            queryset = queryset.filter(owner=user)
        return queryset
    def get_serializer_class(self):
        serializer_class = AdListSerializer
        if self.request.method == 'POST':
            serializer_class = AdCreateSerializer
        return serializer_class

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class AdDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True, context={'request':request})
        return Response(serializer.data)

# class AdListView(APIView):
#     def get(self, request, format=None):
#         queryset = Ad.objects.all()
#         serializer = AdListSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request, format=None):
#         serializer = AdCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             user = self.request.user
#             person = Person.objects.get(id=user.id)
#             serializer.save(person=person)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class AdDetailView(APIView):
#     def get_object(self, uuid):
#         try:
#             return Ad.objects.get(pk=uuid)
#         except Ad.DoesNotExist:
#             raise Http404
#
#     def get(self, request, uuid, format=None):
#         ad = self.get_object(uuid)
#         ad = AdDetailSerializer(ad)
#         return Response(ad.data)
#
#
#     def delete(self, request, uuid, format=None):
#         ad = self.get_object(uuid)
#         print(ad)
#         ad.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def patch(self, request, uuid, format=None):
#         serializer = AdCreateSerializer(data=request.data, partial=True)
#         if serializer.is_valid():
#             user = self.request.user
#             person = Person.objects.get(id=user.id)
#             serializer.save(person=person)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
