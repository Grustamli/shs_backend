from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Ads': reverse('ad_list', request=request, format=format),
        'Categories': reverse('category_list', request=request, format=format),
        'Vehicle Props': reverse('vehicle_props', request=request, format=format)
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
