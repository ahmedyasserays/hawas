from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import (
    HomePageHeroSection,
    HomePageTile,
    NewArrivals,
    PopularProducts,
    AvailableProducts,
)

# Register your models here.
admin.site.register(HomePageTile)

admin.site.register(HomePageHeroSection, SingletonModelAdmin)
admin.site.register(NewArrivals, SingletonModelAdmin)
admin.site.register(PopularProducts, SingletonModelAdmin)
admin.site.register(AvailableProducts)
