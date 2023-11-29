from django.contrib.gis.geos import Point
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
import pyproj
from django.core.serializers import serialize

from home.models import *


class NatoshiSerializer(GeoFeatureModelSerializer):

    # custom_geometry = serializers.SerializerMethodField()

    class Meta:
        model = Natoshi
        geo_field = "geom"
        fields = '__all__'

    def get_custom_geometry(self, obj):
        original_geometry = obj.geom
        transform = serialize("geojson", original_geometry)
        # source_crs = pyproj.CRS(original_geometry.srid)
        # target_crs = pyproj.CRS("EPSG:4326")
        # transformer = pyproj.Transformer.from_crs(
        #     source_crs, target_crs, always_xy=True)
        # transformed_geometry = original_geometry.transform(transformer)
        return transform
