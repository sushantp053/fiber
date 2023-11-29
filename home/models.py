from django.db import models
from django.contrib.gis.db import models
import uuid

# Create your models here.


class Fiber(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    name = models.TextField()
    addr = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()
    type = models.TextField()


# Create your models here.
class Marker(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    name = models.TextField()
    addr = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()
    type = models.TextField(default="1")


class Talav(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    name = models.TextField()
    area = models.TextField()
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'talav'


class Natoshi(models.Model):
    GutNo = models.UUIDField(primary_key=True, unique=True,
                             editable=False, default=uuid.uuid4)
    gutno = models.IntegerField()
    id = models.IntegerField()
    geom = models.MultiPolygonField()
    gut = models.TextField()
    crop = models.TextField()
    owner = models.TextField()
    remark = models.TextField()
    village = models.TextField()
    area = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Natoshi'


class Road(models.Model):
    road_id = models.UUIDField(primary_key=True, unique=True,
                               editable=False, default=uuid.uuid4)
    geom = models.MultiLineStringField()
    id = models.IntegerField()
    remark = models.TextField()

    class Meta:
        managed = False
        db_table = "Road"
