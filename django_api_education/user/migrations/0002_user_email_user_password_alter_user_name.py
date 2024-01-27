# Generated by Django 5.0.1 on 2024-01-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(default="default@example.com", max_length=50),
        ),
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.TextField(default="Guest", max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]