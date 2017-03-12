from django.contrib import admin
# from django.contrib.auth.models import User
from .models.ads import AdImage, Ad, Favourite
from .models.ad_extensions import Property
from .models.categories import Category
from .models.add_on import AddOnType
from .models.property_data import PaymentPeriod
from .models.vehicle_data import *
# Register your models here.


admin.site.register([
    AdImage,
    Ad,
    Favourite,
    Property,
    Category,
    AddOnType,
    PaymentPeriod,
    VehicleMake,
    VehicleModel,
    VehicleBody,
    VehicleTransmission,
    VehicleFuel,
])
