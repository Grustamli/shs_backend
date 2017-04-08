from django.conf.urls               import(url, include)
from rest_framework_swagger.views   import get_swagger_view
from rest_framework                 import routers
from .views.ads                     import (AdListView, AdDetailView)
from .views.api_schema              import *
from .views.categories              import CategoryListView
from .views.vehicle_data            import VehiclePropListView
from .views.user_favorites          import (UserFavoriteListView, UserFavoriteDetailView)
from .views.add_on                  import AddOnListView
from .views.ad_image                import *
from .views.register                import RegisterAPIView
from .views.search_alert            import *
from .views.verify_username         import VerifyUsername
from .views.user_posts              import UserPostsListView
from .views.geolocation             import CityListView
from .views.profile                 import ProfileListCreateAPIView

urlpatterns = [
    url(r'^$', api_root),
    url(r'^register$', RegisterAPIView.as_view(), name='register'),
    url(r'^vehicle-props$', vehicle_props_schema, name='vehicle_props'),
    url(r'^favorites$', favorites_schema, name='favorites'),
    url(r'^posts$', AdListView.as_view(), name='posts_list'),
    url(r'^posts/(?P<pk>[\w-]+)$', AdDetailView.as_view(), name='post_detail'),
    url(r'^favorites/(?P<username>[\w-]+)$', UserFavoriteListView.as_view(), name= "user_favorites"),
    url(r'^favorites/(?P<username>[\w-]+)/(?P<ad_uuid>[\w-]+)$', UserFavoriteDetailView.as_view(), name= "favorites_detail"),
    url(r'^post-images$', AdImageListCreateAPIView.as_view() , name='ad_images'),
    url(r'^post-images/(?P<pk>[\w-]+)$', AdImageDetailApiView.as_view(), name='ad_image_detail'),
    # url(r'^ad-images/(?P<ad_uuid>[\w-]+)/(?P<pk>[0-9]+)$', AdImageDetailApiView.as_view(), name='ad_image_detail'),
    url(r'^add-ons$', AddOnListView.as_view(), name = "add_ons"),
    url(r'^search-alerts$', search_alert_schema, name='search_alerts'),
    url(r'^search-alerts/(?P<username>[\w-]+)$', SearchAlertListView.as_view(), name="user_search_alerts"),
    url(r'^search-alerts/(?P<username>[\w-]+)/(?P<pk>[0-9]+)$', SearchAlertDetailView.as_view(), name="user_search_alerts_detail"),
    url(r'^verify-username', VerifyUsername.as_view(), name='verify_username'),
    url(r'^user-posts/(?P<username>[\w-]+)$', UserPostsListView.as_view(), name='user-posts'),
    url(r'^profiles', ProfileListCreateAPIView.as_view(), name='profile_list')
]

helper_urls = [
    url(r'^categories', CategoryListView.as_view(), name='category_list'),
    url(r'^vehicle-props/(?P<feature>[\w-]+)$', VehiclePropListView.as_view(), name="vehicle_prop"),
    url(r'^cities$', CityListView.as_view(), name='city_list')
]



schema_view = get_swagger_view(title='Bili API', url='/')
urlpatterns += [url(r'^swagger$', schema_view)]
urlpatterns += helper_urls
