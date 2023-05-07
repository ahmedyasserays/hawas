from typing import Any, Dict
from django.views.generic import TemplateView
from store.models import Product
from .models import (
    HomePageHeroSection,
    NewArrivalsSection,
    PopularProductsSection,
    HomePageTile,
    AboutUsHero,
    AboutUsTile,
    Founder,
)


# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["hero_section"] = HomePageHeroSection.get_solo()
        ctx["tiles"] = HomePageTile.objects.all()
        ctx["new_arrivals_section"] = NewArrivalsSection.get_solo()
        ctx["popular_products_section"] = PopularProductsSection.get_solo()
        ctx["new_arrivals"] = (
            Product.objects.available()
            .with_first_image()
            .with_first_color()
            .with_first_size()
            .with_wishlist(self.request)
            .order_by("-created")[:8]
        )
        ctx["popular_products"] = Product.objects.popular().with_first_image()[:8]
        return ctx

class AboutUsView(TemplateView):
    template_name = 'about-us.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['hero_section'] = AboutUsHero.get_solo()
        ctx['tile'] = AboutUsTile.get_solo()
        ctx['founders'] = Founder.objects.all()
        return ctx