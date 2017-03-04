from django.contrib import admin
# from django.contrib.auth.models import User
from .models.ads import AdImage, Ad, Favourite
from .models.ad_extensions import Property
from .models.categories import Category
from .models.add_on import AddOnType
# Register your models here.


admin.site.register([
    AdImage,
    Ad,
    Favourite,
    Property,
    Category,
    AddOnType
])
