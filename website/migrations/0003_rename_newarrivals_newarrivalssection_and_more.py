# Generated by Django 4.1.5 on 2023-05-04 08:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_availableproducts"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NewArrivals",
            new_name="NewArrivalsSection",
        ),
        migrations.RenameModel(
            old_name="PopularProducts",
            new_name="PopularProductsSection",
        ),
        migrations.RenameModel(
            old_name="AvailableProducts",
            new_name="ShopPage",
        ),
    ]