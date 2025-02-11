from rest_framework import viewsets

from .serializers import HealthFacilitiesSerializer

from .models import HealthFacilities


class HealthFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = HealthFacilities.objects.all()
    serializer_class = HealthFacilitiesSerializer
