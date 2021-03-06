from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models.ads import AdImage, Ad, Favourite
from .models.ad_extensions import Property
from .models.categories import Category
from .models.add_on import *
from .models.property_data import PaymentPeriod
from .models.vehicle_data import *
from .models.contact import *
from .models.user import *
from .models.search_alert import SearchAlert


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register([
    AdImage,
    Ad,
    Address,
    PhoneNumber,
    Favourite,
    Property,
    Category,
    AddOnType,
    AppliedAddOn,
    PaymentPeriod,
    VehicleMake,
    VehicleModel,
    VehicleBody,
    VehicleTransmission,
    VehicleFuel,
    SearchAlert
])
