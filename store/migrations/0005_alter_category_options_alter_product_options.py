# Generated by Django 4.1.5 on 2023-02-02 21:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_alter_product_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["order"],
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["order"]},
        ),
    ]