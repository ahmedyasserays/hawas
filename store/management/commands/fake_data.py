import random

from django.core.management.base import BaseCommand
from django.db import transaction

from store.factories import CategoryFactory, ImageFactory, OptionFactory, ProductFactory


class Command(BaseCommand):
    help = "create fake data for testing"

    NUM_CATEGORY = 5
    NUM_PRODUCTS = 50
    NUM_OPTIONS_PER_PRODUCT = 3
    NUM_IMAGES_PER_PRODUCT = 3

    @transaction.atomic
    def handle(self, *args, **options):
        cats = []
        for _ in range(self.NUM_CATEGORY):
            cats.append(CategoryFactory())

        prods = []
        for _ in range(self.NUM_PRODUCTS):
            prod = ProductFactory(category=random.choice(cats))
            prods.append(prod)
            for _ in range(self.NUM_OPTIONS_PER_PRODUCT):
                OptionFactory(product=prod)

            for _ in range(self.NUM_IMAGES_PER_PRODUCT):
                ImageFactory(product=prod)
