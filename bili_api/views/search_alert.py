from rest_framework. generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from ..models.search_alert import SearchAlert
from ..serializers.search_alert import *

class SearchAlertListView(ListCreateAPIView):
    serializer_class = SearchAlertListSerializer
    def get_queryset(self, *args, **kwargs):
        queryset = SearchAlert.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(owner__username=user)
        return queryset
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

class SearchAlertDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SearchAlertDetailSerializer
    queryset = SearchAlert.objects.all()
    def get_object(self):
        pk = self.kwargs['pk']
        try:
            return self.get_queryset.get(pk=pk)
        except SearchAlert.DoesNotExist:
            raise NotFound
