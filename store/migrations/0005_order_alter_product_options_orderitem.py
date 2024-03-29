# Generated by Django 4.1.2 on 2023-02-05 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0004_alter_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("alt_phone", models.CharField(blank=True, max_length=20, null=True)),
                ("country", models.CharField(blank=True, max_length=20, null=True)),
                ("city", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "street_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("zone_number", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "building_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("email", models.EmailField(max_length=254)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("notes", models.CharField(blank=True, max_length=150, null=True)),
                ("fast_delivery", models.BooleanField(default=False)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("cash_on_delivery", "Cash on delivery"),
                            ("online_payment", "Online Payment"),
                        ],
                        default="cash_on_delivery",
                        max_length=150,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("unpaid", "Unpaid"),
                            ("pending", "Pending"),
                            ("paid", "Paid"),
                            ("canceled", "Canceled"),
                            ("pernding_refund", "Pending refund"),
                            ("refunded", "Refunded"),
                            ("delivered", "Delivered"),
                        ],
                        default="unpaid",
                        max_length=150,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["-created", "order"]},
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "option",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="store.option",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="store.order",
                    ),
                ),
            ],
        ),
    ]
