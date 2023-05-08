from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import (
    AboutUsHero,
    AboutUsTile,
    Founder,
    HomePageHeroSection,
    HomePageTile,
    NewArrivalsSection,
    PopularProductsSection,
    ShopPage,
)

# Register your models here.
admin.site.register(HomePageTile)

admin.site.register(HomePageHeroSection, SingletonModelAdmin)
admin.site.register(NewArrivalsSection, SingletonModelAdmin)
admin.site.register(PopularProductsSection, SingletonModelAdmin)
admin.site.register(ShopPage)
admin.site.register(Founder)
admin.site.register(AboutUsTile)
admin.site.register(AboutUsHero)
