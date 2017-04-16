from rest_framework.generics import (ListAPIView, RetrieveUpdateDestroyAPIView)
from ..serializers.profile import (ProfileListSerializer)
from ..models.user import Profile
from django.shortcuts import get_object_or_404

class ProfileListCreateAPIView(ListAPIView):
    queryset            = Profile.objects.all()
    serializer_class    = ProfileListSerializer

class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset            = Profile.objects.all()
    serializer_class    = ProfileListSerializer
    lookup_field        = 'owner__username'
    lookup_url_kwarg   = 'username'
