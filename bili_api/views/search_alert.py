from rest_framework. generics import (ListCreateAPIView, RetrieveDestroyAPIView)
from ..models.search_alert import SearchAlert
from ..serializers.search_alert import *

class SearchAlertListView(ListCreateAPIView):
    serializer_class = SearchAlertListSerializer
    def get_queryset(self, *args, **kwargs):
        queryset = SearchAlert.objects.all()
        user = self.request.query_params.get('user', None)
        search_term = self.request.query_params.get('search-term', None)
        if user is not None:
            queryset = queryset.filter(owner__username=user)
        if search_term is not None:
            queryset = queryset.filter(search_term=search_term)
        return queryset
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

class SearchAlertDetailView(RetrieveDestroyAPIView):
    serializer_class = SearchAlertListSerializer
    queryset = SearchAlert.objects.all()
    def get_object(self):
        pk = self.kwargs['pk']
        try:
            return self.get_queryset().get(pk=pk)
        except SearchAlert.DoesNotExist:
            raise NotFound
