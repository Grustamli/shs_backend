from rest_framework.generics import ListAPIView
from ..models.add_on import AddOnType
from ..serializers.add_on import AddOnListSerializer

class AddOnListView(ListAPIView):
    queryset = AddOnType.objects.all()
    serializer_class = AddOnListSerializer
    
