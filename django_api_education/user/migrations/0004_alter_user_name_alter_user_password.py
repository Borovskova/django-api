# Generated by Django 5.0.1 on 2024-01-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_user_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(default="Guest", max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.TextField(default="password", max_length=50),
        ),
    ]
