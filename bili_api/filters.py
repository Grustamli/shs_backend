from django_filters.rest_framework import FilterSet
import django_filters

from .helpers.getAllSubCategories import get_all_subcategories
from .models.ads import  Ad

class AdFilter(FilterSet):

    min_price = django_filters.NumberFilter(name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(name='price', lookup_expr='lte')
    category = django_filters.CharFilter(method='category_filter')

    def category_filter(self, queryset, name, value):
        sub_cat_names = get_all_subcategories(value)
        filtered_queryset = queryset.filter(category__name__in=sub_cat_names)
        return filtered_queryset

    class Meta:
        model = Ad
        fields = ['category', 'min_price', 'max_price']
#
#
# class PropertyFilter(FilterSet):
#     min_price = django_filters.NumberFilter(name='ad__price', lookup_expr='gte')
#     max_price = django_filters.NumberFilter(name='ad__price', lookup_expr='lte')
#     min_bed_room = django_filters.NumberFilter(name='no_bed_room', lookup_expr='gte')
#     max_bed_room = django_filters.NumberFilter(name='no_bed_room', lookup_expr='lte')
#     min_area = django_filters.NumberFilter(name='area', lookup_expr='gte')
#     max_area = django_filters.NumberFilter(name='area', lookup_expr='lte')
#
#     class Meta:
#         model = Property
#         fields = ['min_price', 'max_price','min_bed_room', 'max_bed_room','min_area',
#                     'max_price', 'no_bed_room', 'payment',]
#
# class VehicleFilter(FilterSet):
#     min_price = django_filters.NumberFilter(name='ad__price', lookup_expr='gte')
#     max_price = django_filters.NumberFilter(name='ad__price', lookup_expr='lte')
#     min_mileage = django_filters.NumberFilter(name='mileage', lookup_expr='gte')
#     max_mileage = django_filters.NumberFilter(name='mileage', lookup_expr='lte')
#     min_year = django_filters.NumberFilter(name='year', lookup_expr='lte')
#     max_year = django_filters.NumberFilter(name='year', lookup_expr='gte')
#     min_engine_size = django_filters.NumberFilter(name='engine_size', lookup_expr='gte')
#     max_engine_size = django_filters.NumberFilter(name='engine_size', lookup_expr='lte')
#
#     class Meta:
#         model = Vehicle
#         fields = ['min_price', 'max_price', 'min_mileage', 'max_mileage', 'min_year', 'max_year',
#                     'min_engine_size', 'max_engine_size', 'ad__category', 'make', 'body', 'fuel', 'transmission']
