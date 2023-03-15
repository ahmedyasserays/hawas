import random
import factory
from factory.django import DjangoModelFactory

from .models import Category, Option, Product, ProductImage


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    name_ar = factory.Faker("name")
    slug = factory.Faker("slug")
    img = factory.django.ImageField()


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("name")
    name_ar = factory.Faker("name")
    slug = factory.Faker("slug")
    category = factory.SubFactory(CategoryFactory)

    describtion = factory.Faker("sentence")
    describtion_ar = factory.Faker("sentence")


class OptionFactory(DjangoModelFactory):
    class Meta:
        model = Option

    name = factory.Faker("name")
    name_ar = factory.Faker("name")
    slug = factory.Faker("slug")
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker("pyint")
    price = factory.LazyAttribute(
        lambda x: random.randrange(1, 10_000) + random.random()
    )

    discount = factory.Faker("pyfloat")


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = ProductImage

    img = factory.django.ImageField()
    product = factory.SubFactory(ProductFactory)
