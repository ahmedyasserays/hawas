# Generated by Django 4.1.2 on 2023-02-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productimage",
            options={"ordering": ("order",)},
        ),
        migrations.AddField(
            model_name="category",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=1, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=1, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productimage",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=1, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
    ]