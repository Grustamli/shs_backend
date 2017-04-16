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


