from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import (
    AboutUsHero,
    AboutUsTile,
    CallTile,
    ContactHero,
    Founder,
    HomePageHeroSection,
    HomePageTile,
    MailTile,
    NewArrivalsSection,
    PopularProductsSection,
    ShopPage,
    ContactMessage,
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
admin.site.register(CallTile)
admin.site.register(MailTile)
admin.site.register(ContactHero)
admin.site.register(ContactMessage)
