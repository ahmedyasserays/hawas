import random

from django.core.management.base import BaseCommand
from django.db import transaction

from store.factories import (
    CategoryFactory,
    ImageFactory,
    ProductFactory,
    ColorFactory,
    SizeFactory,
    ProductReviewFactory,
)
from users.factories import UserFactory


class Command(BaseCommand):
    help = "create fake data for testing"

    NUM_CATEGORY = 5
    NUM_PRODUCTS = 50
    NUM_IMAGES_PER_PRODUCT = 3
    NUM_OF_COLORS = 10
    NUM_OF_SIZES = 5
    NUM_OF_USERS = 5
    NUM_REVIEWS_PER_PRODUCT = 5

    @transaction.atomic
    def handle(self, *args, **options):
        cats = []
        for _ in range(self.NUM_CATEGORY):
            cats.append(CategoryFactory())

        prods = []
        for _ in range(self.NUM_PRODUCTS):
            prod = ProductFactory(category=random.choice(cats))
            prods.append(prod)
            for _ in range(self.NUM_IMAGES_PER_PRODUCT):
                ImageFactory(product=prod)

        colors = []
        for _ in range(self.NUM_OF_COLORS):
            color = ColorFactory()
            colors.append(color)

        sizes = []
        for _ in range(self.NUM_OF_SIZES):
            size = SizeFactory()
            sizes.append(size)

        for prod in prods:
            prod.related_products.set(random.sample(prods, random.randint(0, 15)))
            prod.available_colors.set(
                random.sample(colors, random.randint(0, len(colors)))
            )
            prod.available_sizes.set(
                random.sample(sizes, random.randint(0, len(sizes)))
            )

        users = []
        for _ in range(self.NUM_OF_USERS):
            user = UserFactory()
            users.append(user)

        for prod in prods:
            for user in random.sample(users, self.NUM_REVIEWS_PER_PRODUCT):
                ProductReviewFactory(user=user, product=prod)
