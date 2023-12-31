# Generated by Django 4.2.3 on 2023-08-28 07:00

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_marker_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Talav",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.TextField()),
                ("addr", models.TextField()),
                ("lng", models.FloatField()),
                ("lat", models.FloatField()),
                (
                    "mpoly",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
            options={
                "db_table": "Talav",
                "managed": False,
            },
        ),
    ]
