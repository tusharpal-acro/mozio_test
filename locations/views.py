from rest_framework import viewsets
from locations.models import Locations
from locations.serializers import LocationSerializer
from django.contrib.gis.geos import Point
from rest_framework.decorators import action
from django.http import JsonResponse

# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer

    @action(detail=False)
    def get_location(self, request, **kwargs):
        lat = float(request.query_params["lat"])
        lon = float(request.query_params["lon"])
        result = Locations.objects.filter(point__contains=Point((lat, lon)))
        data = result.values().get()
        data["point"] = data["point"].tuple
        return JsonResponse(data, safe=False)
