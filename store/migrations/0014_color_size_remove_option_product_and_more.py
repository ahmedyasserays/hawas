# Generated by Django 4.1.5 on 2023-04-01 23:19

import autoslug.fields
import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0013_alter_option_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Color",
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
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_ar", models.CharField(max_length=150)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        max_length=100,
                        populate_from="name",
                        unique=True,
                    ),
                ),
                (
                    "code",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=18, samples=None
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "colors",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Size",
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
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_ar", models.CharField(max_length=150)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        max_length=100,
                        populate_from="name",
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "sizes",
                "ordering": ["order"],
            },
        ),
        migrations.RemoveField(
            model_name="option",
            name="product",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="option",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="store.product",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="discount",
            field=models.FloatField(
                default=0,
                validators=[
                    django.core.validators.MaxValueValidator(
                        100, "Can't make discount more than 100%"
                    ),
                    django.core.validators.MinValueValidator(
                        0, "Can't create offer less than 0%"
                    ),
                ],
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.FloatField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(
                        1, "Can't set price less than 1"
                    ),
                    django.core.validators.MaxValueValidator(
                        100000, "Can't set price more than 100000"
                    ),
                ],
            ),
            preserve_default=False,
        ),
    ]