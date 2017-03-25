from rest_framework.generics import ListAPIView
from ..serializers.profile import ProfileListSerializer
from ..models.user import Profile

class ProfileListCreateAPIView(ListAPIView):
    queryset            = Profile.objects.all()
    serializer_class    = ProfileListSerializer
