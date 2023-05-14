# Generated by Django 4.1.5 on 2023-05-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="phonenum",
            name="tile",
        ),
        migrations.AddField(
            model_name="calltile",
            name="phone1",
            field=models.CharField(default="0123456789", max_length=15),
        ),
        migrations.AddField(
            model_name="calltile",
            name="phone2",
            field=models.CharField(default="0123456789", max_length=15),
        ),
        migrations.AddField(
            model_name="mailtile",
            name="mail",
            field=models.EmailField(default="hawas.store.1@gmail.com", max_length=254),
        ),
        migrations.DeleteModel(
            name="Mail",
        ),
        migrations.DeleteModel(
            name="PhoneNum",
        ),
    ]