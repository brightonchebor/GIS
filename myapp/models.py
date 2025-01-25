from django.contrib.gis.db import models as gis_models
from django.db import models


# Model class for factories table in database
class Factory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField()
    geofence = gis_models.PolygonField()

    class Meta:
        db_table = "factories"



