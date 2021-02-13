# Generated by Django 3.1.5 on 2021-02-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libraryApp", "0004_auto_20210213_1210"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="quantity",
        ),
        migrations.AddField(
            model_name="copy",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
    ]
