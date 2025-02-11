from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometryField
from .models import HealthFacilities


class HealthFacilitiesSerializer(GeoFeatureModelSerializer):
    geom = GeometryField()

    class Meta:
        model = HealthFacilities
        geo_field = "geom"
        fields = "__all__"
