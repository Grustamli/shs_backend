from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from ..models.ads import Ad

@api_view(['GET'])
@permission_classes([IsAdminUser,])
def api_root(request, format=None):
    return Response({
        'Posts'             :reverse('posts_list', request=request, format=format),
        'Categories'        :reverse('category_list', request=request, format=format),
        'Vehicle Props'     :reverse('vehicle_props', request=request, format=format),
        'Favorites'         :reverse('favorites', request=request, format=format),
        'Add Ons'           :reverse('add_ons', request=request, format=format),
        'Ad Images'         :reverse('ad_images', request=request, format=format),
        'Register'          :reverse('register', request=request, format=format),
        'Cities'            :reverse('city_list', request=request, format=format),
        'Profiles'          :reverse('profile_list', request=request, format=format)
    })

@api_view(['GET'])
@permission_classes([IsAdminUser,])
def vehicle_props_schema(request, format=None):
    return Response({
        'Make'              :reverse('vehicle_prop', kwargs={'feature': 'make'}, request=request, format=format),
        'Body'              :reverse('vehicle_prop', kwargs={'feature': 'body'}, request=request, format=format),
        'Fuel'              :reverse('vehicle_prop', kwargs={'feature': 'fuel'}, request=request, format=format),
        'Model'             :reverse('vehicle_prop', kwargs={'feature': 'model'}, request=request, format=format),
        'Transmission'      :reverse('vehicle_prop', kwargs={'feature': 'transmission'}, request=request, format=format),
    })


@api_view(['GET'])
@permission_classes([IsAdminUser,])
def favorites_schema(request, format=None):
    users                   = User.objects.all()
    urls                    = {}
    for user in users:
        username            = user.username
        urls[username]      = reverse('user_favorites', kwargs={'username': username}, request=request, format=format)
    return Response(urls)
