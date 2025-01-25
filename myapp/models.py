from django.contrib.gis.db import models as gis_models
from django.db import models
import uuid

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    geometry = gis_models.PointField() 

class Factory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

