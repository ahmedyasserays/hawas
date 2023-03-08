# Generated by Django 4.1.2 on 2023-02-05 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_popular_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="popular_products",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="popular_products",
                to="store.product",
            ),
        ),
    ]