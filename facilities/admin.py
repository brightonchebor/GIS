from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import HealthFacilities


class HealthFacilitiesAdmin(LeafletGeoAdmin):
    list_display = ("name", "healthcare")


admin.site.register(HealthFacilities, HealthFacilitiesAdmin)
