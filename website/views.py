from django.views.generic import TemplateView, CreateView, ListView, DetailView
from store.models import Product
from website.forms import ContactForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .models import (
    Blog,
    ContactMessage,
    HomePageHeroSection,
    NewArrivalsSection,
    PopularProductsSection,
    HomePageTile,
    AboutUsHero,
    AboutUsTile,
    Founder,
    MailTile,
    CallTile,
    ContactHero,
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
    template_name = "about-us.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["hero_section"] = AboutUsHero.get_solo()
        ctx["tile"] = AboutUsTile.get_solo()
        ctx["founders"] = Founder.objects.all()
        return ctx


class ContactUsView(TemplateView):
    template_name = "contact-us.html"

    

class ContactMessageView(CreateView):
    template_name = "contact-us.html"
    model = ContactMessage
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
            ctx["hero_section"] = ContactHero.get_solo()
            ctx["mail"] = MailTile.get_solo()
            ctx["call"] = CallTile.get_solo()
            return ctx
# TODO: add success popup
# TODO: make send_message background task    
    def form_valid(self, form):
        res = super().form_valid(form)
        # TODO:change form_email and recipient_list
        send_mail(
            subject=f"New message from {form.cleaned_data['name']} ({form.cleaned_data['email']})",
            message=form.cleaned_data["message"],
            from_email="nitox56@gmail.com",
            recipient_list=["hawas.store.1@gmail.com"],
            fail_silently=False,
        )
        return res


class BlogListView(ListView):
    template_name = "blogs.html"
    model = Blog
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    template_name = "blog.html"
    model = Blog
    context_object_name = "blog"
