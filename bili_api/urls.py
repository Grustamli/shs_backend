from django.conf.urls import(url, include)
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from .views.ads import (AdListView, AdDetailView)
from .views.api_schema import *
from .views.categories import CategoryListView
from .views.vehicle_data import VehiclePropListView
from .views.user_favorites import (UserFavoriteListView, UserFavoriteDetailView)
from .views.add_on import AddOnListView
from .views.ad_image import (AdImageListApiView, AdImageDetailApiView)
from .views.register import RegisterListView
from .views.search_alert import *
from .views.verify_username import VerifyUsername
from .views.ad_extensions import *

urlpatterns = [
 url(r'^$', api_root),
 url(r'^register/$', RegisterListView.as_view(), name='register'),
 url(r'^vehicle-props/$', vehicle_props_schema, name='vehicle_props'),
 url(r'^favorites/$', favorites_schema, name='favorites'),
 url(r'^ads/$', AdListView.as_view(), name='ad_list'),
 url(r'^ads/(?P<pk>[\w-]+)/$', AdDetailView.as_view(), name='ad_detail'),
 url(r'^categories/', CategoryListView.as_view(), name='category_list'),
 url(r'^vehicle-props/(?P<feature>[\w-]+)/$', VehiclePropListView.as_view(), name="vehicle_prop"),
 url(r'^favorites/(?P<username>[\w-]+)/$', UserFavoriteListView.as_view(), name= "user_favorites"),
 url(r'^favorites/(?P<username>[\w-]+)/(?P<pk>[0-9]+)/$', UserFavoriteDetailView.as_view(), name= "favorites_detail"),
 url(r'^ad-images/$', ad_images, name='ad_images'),
 url(r'^ad-images/(?P<ad_uuid>[\w-]+)/$', AdImageListApiView.as_view(), name='ad_image_list'),
 url(r'^ad-images/(?P<ad_uuid>[\w-]+)/(?P<pk>[0-9]+)/$', AdImageDetailApiView.as_view(), name='ad_image_detail'),
 url(r'^add-ons/$', AddOnListView.as_view(), name = "add_ons"),
 url(r'^search-alerts/$', search_alert_schema, name='search_alerts'),
 url(r'^search-alerts/(?P<username>[\w-]+)/$', SearchAlertListView.as_view(), name="user_search_alerts"),
 url(r'^search-alerts/(?P<username>[\w-]+)/(?P<pk>[0-9]+)/$', SearchAlertDetailView.as_view(), name="user_search_alerts_detail"),
 url(r'^verify-username', VerifyUsername.as_view(), name='verify_username'),
 url(r'^vehicle-ads/', VehicleAdListCreateView.as_view(), name='vehicle_ads'),
 url(r'^property-ads/', PropertyAdListCreateView.as_view(), name='property_ads')
]


schema_view = get_swagger_view(title='Bili API', url='/')
urlpatterns += [url(r'^swagger$', schema_view)]
