# Generated by Django 5.0.1 on 2024-01-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_name_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.IntegerField(default=0),
        ),
    ]