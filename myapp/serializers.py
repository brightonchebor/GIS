from rest_framework import serializers
from .models import Factory, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'geometry']

class FactorySerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Factory
        fields = ['id', 'name', 'location']