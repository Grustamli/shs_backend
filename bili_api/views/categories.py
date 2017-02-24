from rest_framework.generics import ListAPIView
from ..models.categories import Category
from ..serializers.categories import CategoryListSerializer


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer
    def get_queryset(self):
        queryset = Category.objects.all()
        current = self.request.query_params.get('current', None)
        if current is not None:
            current_obj = queryset.get(pk=current)
            queryset = current_obj.subcategories
        return queryset
