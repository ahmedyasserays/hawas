import random
import factory
from factory.django import DjangoModelFactory

from users.factories import UserFactory

from .models import Category, ProductReview, Size, Color, Product, ProductImage


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")
    name_ar = factory.Faker("word")
    slug = factory.Faker("slug")
    img = factory.django.ImageField()


class SizeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Size

    name = factory.Faker("word")
    name_ar = factory.Faker("word")


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color

    name = factory.Faker("color_name")
    name_ar = factory.Faker("word")
    code = factory.Faker("hex_color")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    name_ar = factory.Faker("word")
    slug = factory.Faker("slug")
    category = factory.SubFactory(CategoryFactory)
    describtion = factory.Faker("text")
    describtion_ar = factory.Faker("text")
    available = factory.Faker("pybool")
    price = factory.LazyAttribute(
        lambda x: random.randrange(1, 10_000) + random.random()
    )
    discount = factory.LazyAttribute(
        lambda x: random.randrange(0, 100) + random.random()
    )
    visits = factory.Faker('pyint', min_value=0)


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = ProductImage

    img = factory.django.ImageField()
    product = factory.SubFactory(ProductFactory)


class ProductReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductReview

    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    rate = factory.Faker('pyint', min_value=1, max_value=5)
    comment = factory.Faker('text')
