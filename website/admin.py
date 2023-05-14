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
    Blog
)

# Register your models here.
admin.site.register(HomePageTile)

admin.site.register(HomePageHeroSection, SingletonModelAdmin)
admin.site.register(NewArrivalsSection, SingletonModelAdmin)
admin.site.register(PopularProductsSection, SingletonModelAdmin)
admin.site.register(ShopPage, SingletonModelAdmin)
admin.site.register(Founder)
admin.site.register(AboutUsTile, SingletonModelAdmin)
admin.site.register(AboutUsHero, SingletonModelAdmin)
admin.site.register(CallTile, SingletonModelAdmin)
admin.site.register(MailTile, SingletonModelAdmin)
admin.site.register(ContactHero, SingletonModelAdmin)
admin.site.register(ContactMessage)
admin.site.register(Blog)
