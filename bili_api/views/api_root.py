from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ads': reverse('ad_list', request=request, format=format),
        'categories': reverse('category_list', request=request, format=format),
        'vehicle_make': reverse('vehicle_props', kwargs={'feature': 'make'}, request=request, format=format),
        'vehicle_body': reverse('vehicle_props', kwargs={'feature': 'body'}, request=request, format=format),
        'vehicle_fuel': reverse('vehicle_props', kwargs={'feature': 'fuel'}, request=request, format=format),
        'vehicle_model': reverse('vehicle_props', kwargs={'feature': 'model'}, request=request, format=format),
        'vehicle_transmission': reverse('vehicle_props', kwargs={'feature': 'transmission'}, request=request, format=format),

    })
