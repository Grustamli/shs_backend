from django.contrib import admin
from .models.user import Person
from .models.ads import AdImage, Ad, Favourite
from .models.detailed_ads import Property
from .models.categories import (MainCategory, SubCategory)
# Register your models here.

admin.site.register([
                    Person,
                    AdImage,
                    Ad,
                    Favourite,
                    Property,
                    MainCategory,
                    SubCategory,
                    ])
