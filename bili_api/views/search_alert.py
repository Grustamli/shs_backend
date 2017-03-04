from rest_framework. generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from ..models.search_alert import SearchAlert
from ..serializers.search_alert import *

class SearchAlertListView(ListCreateAPIView):
    serializer_class = SearchAlertListSerializer
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs['username']
        queryset = SearchAlert.objects.all()
        search_alerts = queryset.filter(owner__username=username)
        return search_alerts

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

class SearchAlertDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SearchAlertDetailSerializer
    def get_object(self):
        username = self.kwargs['username']
        sa_id = self.kwargs['pk']
        sa_queryset = SearchAlert.objects.filter(owner__username=username)
        try:
            return sa_queryset.get(id=sa_id)
        except SearchAlert.DoesNotExist:
            raise NotFound
