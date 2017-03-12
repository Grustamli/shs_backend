from rest_framework.generics import ListAPIView
from ..serializers.ads import AdListSerializer
from ..models.ads import Ad

class UserPostsListView(ListAPIView):
    serializer_class = AdListSerializer
    queryset = Ad.objects.all()

    def get_queryset(self):
        username = self.kwargs['username']
        if username is not None:
            queryset = Ad.objects.filter(owner__username=username)
        return queryset

        
