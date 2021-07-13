from locations.models import Locations
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Locations
        geo_field = "point"
        fields = "__all__"
        exclude = ()
