# Generated by Django 4.1.5 on 2023-03-11 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0012_alter_option_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="option",
            name="price",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, "Can't set price less than 1"
                    ),
                    django.core.validators.MaxValueValidator(
                        100000, "Can't set price more than 100000"
                    ),
                ]
            ),
        ),
    ]