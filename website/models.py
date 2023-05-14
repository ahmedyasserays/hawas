from django.db import models
from django.urls import reverse
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


class AboutUsHero(SingletonModel):
    title = models.CharField(max_length=100, default="Hero_Section")
    description = models.TextField(default=LOREM)
    image = models.ImageField(upload_to="defaults", default="defaults/shop-bg.jpg")


class AboutUsTile(SingletonModel):
    title = models.CharField(max_length=100, default="About_Us_Tile")
    description = models.TextField(default=LOREM)
    image = models.ImageField(upload_to="defaults", default="defaults/shop-bg.jpg")


class Founder(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=LOREM)
    image = models.ImageField(upload_to="defaults", default="defaults/founder.png")
    face_icon = models.URLField(null=True)
    insta_icon = models.URLField(null=True)
    twit_icon = models.URLField(null=True)


class ContactHero(SingletonModel):
    title = models.CharField(max_length=100, default="Contact-Us-Hero")
    description = models.TextField(default=LOREM)
    image = models.ImageField(upload_to="defaults", default="defaults/shop-bg.jpg")

class CallTile(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(default=LOREM)
    phone1 = models.CharField(max_length=15, default='0123456789')
    phone2 = models.CharField(max_length=15, default='0123456789')


class MailTile(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(default=LOREM)
    mail = models.EmailField(default='hawas.store.1@gmail.com')

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    def get_absolute_url(self):
        return reverse('contact')