# Generated by Django 4.2.3 on 2023-08-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_marker"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marker",
            name="type",
            field=models.TextField(default="1"),
        ),
    ]