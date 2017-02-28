from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from ..models.user import Person
from ..models.ads import Ad

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Ads': reverse('ad_list', request=request, format=format),
        'Categories': reverse('category_list', request=request, format=format),
        'Vehicle Props': reverse('vehicle_props', request=request, format=format),
        'Favorites': reverse('favorites', request=request, format=format),
        'Add Ons': reverse('add-ons', request=request, format=format),
        'Ad Images': reverse('ad_images', request=request, format=format)
    })

@api_view(['GET'])
def vehicle_props_schema(request, format=None):
    return Response({
        'Make': reverse('vehicle_prop', kwargs={'feature': 'make'}, request=request, format=format),
        'Body': reverse('vehicle_prop', kwargs={'feature': 'body'}, request=request, format=format),
        'Fuel': reverse('vehicle_prop', kwargs={'feature': 'fuel'}, request=request, format=format),
        'Model': reverse('vehicle_prop', kwargs={'feature': 'model'}, request=request, format=format),
        'Transmission': reverse('vehicle_prop', kwargs={'feature': 'transmission'}, request=request, format=format),
    })


@api_view(['GET'])
def favorites_schema(request, format=None):
    users = Person.objects.all()
    urls = {}
    for user in users:
        user_id = user.id
        urls[user_id] = reverse('user_favorites', kwargs={'user_id': user_id}, request=request, format=format)
    return Response(urls)

@api_view(['GET'])
def ad_images(request, format=None):
    ads = Ad.objects.all()
    urls = {}
    for ad in ads:
        ad_id = ad.id
        urls[ad_id] = reverse('ad_image_list', kwargs={'ad_id': ad_id}, request=request, format=format)
    return Response(urls)
