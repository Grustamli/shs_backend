from rest_framework.generics import ListAPIView
from ..models.categories import Category
from ..serializers.categories import CategoryListSerializer


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer
    def get_queryset(self):
        queryset = Category.objects.all()
        parent = self.request.query_params.get('parent', None)
        if parent is not None:
            if parent == 'null':
                queryset = queryset.filter(parent=None)
            else:
                queryset = queryset.filter(parent=parent)
        return queryset
        
