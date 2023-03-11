# Generated by Django 4.1.5 on 2023-03-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomePageHeroSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum, illum optio eum magni quidem dolorum accusantium omnis"
                    ),
                ),
                ("button_url", models.URLField(default="/shop/")),
                ("button_text", models.CharField(default="Shop Now", max_length=100)),
                (
                    "image",
                    models.ImageField(default="defaults/hero.png", upload_to="hero"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HomePageTile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="tiles")),
            ],
        ),
        migrations.CreateModel(
            name="NewArrivals",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="New Arrivals", max_length=100)),
                (
                    "description",
                    models.TextField(
                        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum, illum optio eum magni quidem dolorum accusantium omnis"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PopularProducts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="Popular Products", max_length=100)),
                (
                    "description",
                    models.TextField(
                        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum, illum optio eum magni quidem dolorum accusantium omnis"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]