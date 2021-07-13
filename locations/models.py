# from django.db import models
from providers.models import Provider
from django.contrib.gis.db import models

# Create your models here.
class Locations(models.Model):
    provider = models.ForeignKey(to=Provider, on_delete=models.CASCADE)
    name = models.CharField("language", max_length=250)
    point = models.PointField()
