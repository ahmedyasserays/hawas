# Generated by Django 4.1.5 on 2023-04-16 01:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_cartitem_unique_together_remove_user_cart_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CartItem",
        ),
    ]
