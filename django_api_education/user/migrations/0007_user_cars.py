# Generated by Django 5.0.1 on 2024-01-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0001_initial"),
        ("user", "0006_alter_user_age_alter_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="cars",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="owners", to="car.car"
            ),
        ),
    ]
