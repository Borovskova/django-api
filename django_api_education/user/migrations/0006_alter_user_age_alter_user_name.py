# Generated by Django 5.0.1 on 2024-01-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_user_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                blank=True, default="Guest", max_length=50, null=True
            ),
        ),
    ]
