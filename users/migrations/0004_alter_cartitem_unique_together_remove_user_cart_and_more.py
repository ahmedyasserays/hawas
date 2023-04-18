# Generated by Django 4.1.5 on 2023-04-01 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0014_color_size_remove_option_product_and_more"),
        ("users", "0003_remove_billingaddress_country_remove_user_about_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="cartitem",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="user",
            name="cart",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="color",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.color",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.product",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cartitem",
            name="size",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="store.size"
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="cartitem",
            unique_together={("user", "product", "color", "size")},
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="option",
        ),
    ]