from django.contrib import admin
from .models.user import Person
from .models.ads import AdImage, Ad, Favourite
from .models.ad_extensions import Property
from .models.categories import Category
from .models.add_on import AddOnType
# Register your models here.


admin.site.register([
    Person,
    AdImage,
    Ad,
    Favourite,
    Property,
    Category,
    AddOnType
])
