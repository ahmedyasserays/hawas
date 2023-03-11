from django.views.generic import TemplateView

from store.models import Product

from .models import HomePageHeroSection, NewArrivals, PopularProducts, HomePageTile


# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["hero_section"] = HomePageHeroSection.get_solo()
        ctx["tiles"] = HomePageTile.objects.all()
        ctx["new_arrivals_section"] = NewArrivals.get_solo()
        ctx["popular_products_section"] = PopularProducts.get_solo()
        ctx["new_arrivals"] = (
            Product.objects.available()
            .with_first_image()
            .with_price()
            .order_by("-created")[:8]
        )
        ctx["popular_products"] = (
            Product.objects.popular().with_first_image().with_price()[:8]
        )
        return ctx
