from django.db import models
from solo.models import SingletonModel

# Create your models here.
LOREM = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum, illum optio eum magni quidem dolorum accusantium omnis"


class HomePageHeroSection(SingletonModel):
    description = models.TextField(default=LOREM)
    button_url = models.URLField(default="/shop/")
    button_text = models.CharField(max_length=100, default="Shop Now")

    # TODO: use https://github.com/matthewwithanm/django-imagekit
    image = models.ImageField(upload_to="hero", default="defaults/hero.png")


# TODO: use this in homepage
class HomePageTile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="tiles")


class NewArrivalsSection(SingletonModel):
    title = models.CharField(max_length=100, default="New Arrivals")
    description = models.TextField(default=LOREM)


class PopularProductsSection(SingletonModel):
    title = models.CharField(max_length=100, default="Popular Products")
    description = models.TextField(default=LOREM)


class ShopPage(SingletonModel):
    title = models.CharField(max_length=100, default="Available Products")
    description = models.TextField(default=LOREM)
    image = models.ImageField(upload_to="shop_page", default="defaults/shop-bg.jpg")
