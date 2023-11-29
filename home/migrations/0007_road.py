# Generated by Django 4.2.3 on 2023-08-31 08:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_natoshi"),
    ]

    operations = [
        migrations.CreateModel(
            name="Road",
            fields=[
                (
                    "road_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326),
                ),
                ("id", models.IntegerField()),
                ("remark", models.TextField()),
            ],
            options={
                "db_table": "Road",
                "managed": False,
            },
        ),
    ]