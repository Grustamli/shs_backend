# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
#
# from rest_framework import viewsets
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.decorators import (api_view, permission_classes)
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
# from rest_framework.permissions import (IsAdminUser, IsAuthenticatedOrReadOnly)
# from rest_framework import filters
#
# from django_filters.rest_framework import (
#                         DjangoFilterBackend,
#                         )
#
# from .serializers import (
#                         RegisterSerializer,
#                         ProfileListSerializer,
#                         ProfileDetailSerializer,
#                         PhoneNumberListSerializer,
#                         PhoneNumberDetailSerializer,
#                         UserAddressListSerializer,
#                         UserAddressDetailSerializer,
#                         AdListSerializer,
#                         AdDetailSerializer,
#                         AdImageListSerializer,
#                         AdImageDetailSerializer,
#                         FavouriteListSerializer,
#                         FavouriteDetailSerializer,
#                         CategorySerializer,
#                         PropertyListSerializer,
#                         PropertyCreateSerializer,
#                         PropertyDetailSerializer,
#                         PropertyUpdateSerializer,
#                         VehicleListSerializer,
#                         VehicleCreateSerializer,
#                         VehicleDetailSerializer,
#                         VehicleUpdateSerializer,
#                         )
#
# from .models.user import (
#                         Person,
#                         PhoneNumber,
#                         UserAddress,
#                         )
#
# from .models.ads import (
#                         Ad,
#                         AdImage,
#                         Favourite
#                         )
#
# from .models.categories import Category
#
#
# from .models.ad_extensions import (
#                         Property,
#                         Vehicle
#                         )
#
# from .permissions import (
#                         IsOwnProfileOrReadOnly,
#                         IsOwnerOrReadOnly,
#                         IsAdOwnerOrReadOnly,
#                         IsOwner,
#                         CanOnlyCreate
#                         )
#
# from .filters import (
#                         AdFilter,
#                         PropertyFilter,
#                         VehicleFilter,
#                         )
#
# from .pagination import CustomAdPagination
#
# # from oauth2_provider.ext.rest_framework import (
# #                         TokenHasReadWriteScope,
# #                         TokenHasScope
# #                         )
#
#
# @api_view(['GET'])
# # @permission_classes((IsAdminUser,))
# def api_root(request, format=None):
#     return Response({
#         'profiles': reverse('profile-list', request=request, format=format),
#         'phonenumbers': reverse('phone-list', request=request, format=format),
#         'addresses': reverse('address-list', request=request, format=format),
#         'ads': reverse('ad-list', request=request, format=format),
#         'ad-images': reverse('adimage-list', request=request, format=format),
#         'favourites': reverse('favourite-list', request=request, format=format),
#         'categories': reverse('category-list', request=request, format=format),
#         'properties': reverse('property-list', request=request, format=format),
#         'vehicles': reverse('vehicle-list', request=request, format=format),
#
#     })
#
#
# class RegisterView(generics.CreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = RegisterSerializer
#
#
# class ProfileListView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = ProfileListSerializer
#     permission_classes=(IsAdminUser,)
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('__all__')
#
# # class ProfileCreateView(generics.CreateAPIView):
# #     queryset = Person.objects.all()
# #     serializer_class = ProfileListSerializer
#
# class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = ProfileDetailSerializer
#     lookup_field = 'username'
#     permission_classes = (IsOwnProfileOrReadOnly,)
#
#
# class PhoneNumberListView(generics.ListAPIView):
#     queryset = PhoneNumber.objects.all()
#     serializer_class = PhoneNumberListSerializer
#     permission_classes = (IsAdminUser,)
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('__all__')
#
#
#
# class PhoneNumberCreateView(generics.CreateAPIView):
#     queryset = PhoneNumber.objects.all()
#     serializer_class = PhoneNumberListSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(person=self.request.user)
#
#
# class PhoneNumberDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PhoneNumber.objects.all()
#     serializer_class = PhoneNumberDetailSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#
#
# class AddressListView(generics.ListAPIView):
#     queryset = UserAddress.objects.all()
#     serializer_class = UserAddressListSerializer
#     permission_classes = (IsAdminUser,)
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('__all__')
#
#
# class AddressCreateView(generics.CreateAPIView):
#     queryset = UserAddress.objects.all()
#     serializer_class = UserAddressListSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(person=self.request.user)
#
#
#
# class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserAddress.objects.all()
#     serializer_class = UserAddressDetailSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#
#
# class AdListView(generics.ListCreateAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdListSerializer
#     lookup_field='slug'
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
#     filter_class = AdFilter
#     pagination_class = CustomAdPagination
#     ordering_fields = ('price', 'published')
#     ordering = ('published',)
#     search_fields = ('title', 'description', 'category__name', 'address__address',
#                     'address__region', 'address__city')
#
#     def perform_create(self, serializer):
#         serializer.save(person=self.request.user)
#
#
# class AdCreateView(generics.CreateAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdListSerializer
#     lookup_field='slug'
#
#     def perform_create(self, serializer):
#         serializer.save(person=self.request.user)
#
#
#
# class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdDetailSerializer
#     lookup_field='slug'
#     permission_classes = (IsOwnerOrReadOnly,)
#
#
# class AdImageListView(generics.ListAPIView):
#     queryset = AdImage.objects.all()
#     serializer_class = AdImageListSerializer
#     permission_classes = (IsAdminUser,)
#
# class AdImageCreateView(generics.CreateAPIView):
#     queryset = AdImage.objects.all()
#     serializer_class = AdImageListSerializer
#
#
# class AdImageDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AdImage.objects.all()
#     serializer_class = AdImageDetailSerializer
#     permission_classes = (IsAdOwnerOrReadOnly,)
#
# class FavoriteListView(generics.ListAPIView):
#     queryset = Favourite.objects.all()
#     serializer_class = FavouriteListSerializer
#     permission_classes = (IsAdminUser,)
#     filter_fields = ('person',)
#
# class FavoriteCreateView(generics.CreateAPIView):
#     queryset = Favourite.objects.all()
#     serializer_class = FavouriteListSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(person=self.request.user)
#
#
#
# class FavouriteDetailView(generics.RetrieveDestroyAPIView):
#     queryset = Favourite.objects.all()
#     serializer_class = FavouriteDetailSerializer
#     permission_classes = (IsOwner,)
#
#
# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class CategoryDetailView(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field='name'
#
#
# class PropertyListView(generics.ListCreateAPIView):
#     queryset = Property.objects.all()
#     serializer_class = PropertyListSerializer
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
#     filter_class = PropertyFilter
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     pagination_class= CustomAdPagination
#     ordering_fields = ('ad__price', 'ad__published')
#     ordering = ('ad__published',)
#     search_fields = ('ad__title', 'ad__description', 'ad__category__name', 'ad__address__address',
#                     'ad__address__region', 'ad__address__city', 'kind', 'status', 'payment')
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return PropertyCreateSerializer
#         return super(PropertyListView, self).get_serializer_class()
#
#     def perform_create(self, serializer):
#         serializer.save(person=self.request.user)
#
#
#
#
# class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Property.objects.all()
#     serializer_class = PropertyDetailSerializer
#     lookup_field = 'id'
#     permission_classes = (IsAdOwnerOrReadOnly,)
#     def get_serializer_class(self):
#         if self.request.method == 'PUT':
#             return PropertyUpdateSerializer
#         return super(PropertyDetailView, self).get_serializer_class()
#
#
# class VehicleListView(generics.ListCreateAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleListSerializer
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
#     filter_class = VehicleFilter
#     pagination_class = CustomAdPagination
#     ordering_fields = ('ad__price', 'ad__published')
#     ordering = ('ad__published',)
#     search_fields = ('ad__title', 'ad__description','ad__category__name','ad__address__address',
#                     'ad__address__region', 'ad__address__city', 'make', 'body', 'fuel', 'transmission')
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return VehicleCreateSerializer
#         return super(VehicleListView, self).get_serializer_class()
#
#     def perform_create(self, serializer):
#         serializer.save(person=self.request.user)
#
#
# class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Property.objects.all()
#     serializer_class = VehicleDetailSerializer
#     lookup_field = 'id'
#     permission_classes = (IsAdOwnerOrReadOnly,)
#     def get_serializer_class(self):
#         if self.request.method == 'PUT':
#             return VehicleUpdateSerializer
#         return super(VehicleDetailView, self).get_serializer_class()
